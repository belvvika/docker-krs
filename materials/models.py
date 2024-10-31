from django.db import models

class Course(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название курса',
        help_text='Введите название курса'
    )
    preview = models.ImageField(
        upload_to='courses/preview',
        blank=True,
        null=True,
        verbose_name='Превью курса',
        help_text='Загрузите превью курса'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание курса',
        help_text='Введите описание курса'
    )
    lessons = models.CharField(
        max_length=100,
        verbose_name='Уроки',
        help_text='Введите уроки курса',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

class Lesson(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название урока',
        help_text='Введите название урока'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание урока',
        help_text='Введите описание урока'
    )
    preview = models.ImageField(
        upload_to='lessons/preview',
        blank=True,
        null=True,
        verbose_name='Превью урока',
        help_text='Загрузите превью урока'
    )
    course_link = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Ссылка на курс',
        help_text='Выберите курс из списка'
    )

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'