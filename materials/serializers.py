from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson

class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class CourseSerializer(ModelSerializer):
    lessons = LessonSerializer()
    class Meta:
        model = Course
        fields = '__all__'

class CourseDetailSerializer(ModelSerializer):
    number_of_lessons = SerializerMethodField()
    lessons = LessonSerializer()

    def get_number_of_lessons(self, course):
        return Course.objects.filter(lessons=course.lessons).count()
    class Meta:
        model = Course
        fields = ('name', 'description', 'lessons', 'number_of_lessons')
