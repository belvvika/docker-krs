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
    lessons = LessonSerializer(source='lesson_set', read_only=True, many=True)

    def get_number_of_lessons(self, course):
            return Lesson.objects.filter(course_link=course).count()
    class Meta:
        model = Course
        fields = ('name', 'description', 'lessons', 'number_of_lessons')
