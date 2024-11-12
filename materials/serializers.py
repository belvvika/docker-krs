from rest_framework import serializers

from materials.validators import validate_links
from materials.models import Course, Lesson, Subscribe

class LessonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[validate_links])
    class Meta:
        model = Lesson
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer()
    class Meta:
        model = Course
        fields = '__all__'

class CourseDetailSerializer(serializers.ModelSerializer):
    number_of_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', read_only=True, many=True)

    def get_number_of_lessons(self, course):
            return Lesson.objects.filter(course_link=course).count()
    class Meta:
        model = Course
        fields = ('name', 'description', 'lessons', 'number_of_lessons')

class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'