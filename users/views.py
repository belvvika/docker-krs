from rest_framework import filters
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from users.models import Payments, User
from users.serializers import UserSerializer

class UserCreateAPIView(CreateAPIView):
    serializer = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ('date_payment')
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')

