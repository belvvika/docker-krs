from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson, Subscribe
from materials.paginations import CustomPagination
from materials.serializers import CourseSerializer, LessonSerializer, CourseDetailSerializer, SubscribeSerializer
from users.permissions import IsModer, IsOwner
from materials.tasks import send_information_about_update


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CourseDetailSerializer
        return CourseSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            self.permission_classes = (~IsModer,)
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (IsModer | IsOwner,)
        elif self.action == 'destroy':
            self.permission_classes = (~IsModer | IsOwner,)
        return super().get_permissions()

    @action(detail=True, methods=('post',))
    def subscribe(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        if course.subscribe.filter(pk=request.user.pk).exists():
            course.subscribe.remove(request.user)
        else:
            course.subscribe.add(request.user)
            send_information_about_update.delay(request.user.email)
        serializer = self.get_serializer(course)
        return Response(serializer.data)

class LessonCreateApiView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (~IsModer, IsAuthenticated)

class LessonListApiView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = CustomPagination

class LessonRetrieveApiView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModer | IsOwner)

class LessonUpdateApiView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModer | IsOwner)

class LessonDestroyApiView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsOwner | ~IsModer)

class SubscribeAPIView(APIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        course_id = request.data.get('course')
        course_item = get_object_or_404(Course, id=course_id)

        subs_item = Subscribe.objects.filter(user=user, course=course_item).exists()

        if subs_item:
            Subscribe.objects.filter(user=user, course=subs_item).delete()
            message = 'Подписка отменена'
        else:
            Subscribe.objects.create(user=user, course=course_item)
            message = 'Подписка оформлена'
        return Response({'message': message})
