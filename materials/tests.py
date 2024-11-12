from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User
from materials.models import Course, Lesson, Subscribe
class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='admin@example.com')
        self.course = Course.objects.create(name='New course', description='New course for beginner programmers')
        self.lesson = Lesson.objects.create(name='First lesson', description='First lesson in the course', course_link=self.course)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('materials:lessons_retrieve', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_lesson_create(self):
        url = reverse('materials:lessons_create')
        data = {
            'name': 'New lesson',
            'description': 'New lesson in the course',
            'course_link': self.course.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.count(), 2
        )

    def test_lesson_update(self):
        url = reverse('materials:lessons_update', args=(self.lesson.pk,))
        data = {
            'name': 'New lesson',
            'description': 'New lesson in the course',
            'course_link': self.course.pk
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), 'New lesson'
        )

    def test_lesson_delete(self):
        url = reverse('materials:lessons_delete', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lesson_list(self):
        url = reverse('materials:lessons_list')
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

class SubscribeTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(email='admin@example.com')
        self.course = Course.objects.create(name='New course', description='New course for beginner programmers')
        self.lesson = Lesson.objects.create(name='First lesson', description='First lesson in the course', course_link=self.course)
        self.subscribe = Subscribe.objects.create(link_to_course=self.course, link_to_user=self.user)
        self.client.force_authenticate(user=self.user)

        def test_subscribe():
            Subscribe.objects.all().delete()
            url = reverse('materials:subscribe_create')
            data = {
                'link_to_course': self.course.pk,
                'link_to_user': self.user.pk
            }
            response = self.client.post(url, data)
            self.assertEqual(
                response.status_code, status.HTTP_200_OK
            )
            self.assertEqual(
                response.data['message'], 'Подписка оформлена'
            )
            self.assertTrue(
                Subscribe.objects.filter(link_to_course=self.course, link_to_user=self.user).exists()
            )
            url = reverse('materials: subscribe_create')
            data = {
                'link_to_course': self.course.pk,
                'link_to_user': self.user.pk
            }
            response = self.client.post(url, data)
            self.assertEqual(
                response.status_code, status.HTTP_200_OK
            )
            self.assertEqual(
                response.data['message'], 'Подписка отменена'
            )
