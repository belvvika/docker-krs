from django.contrib.auth.models import AbstractUser
from django.db import models
from materials.models import Course, Lesson
class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='Почта',
        help_text='Введите вашу электронную почту'
    )
    phone = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name='Номер телефона',
        help_text='Введите ваш номер телефона'
    )
    city = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Город',
        help_text='Введите ваш город'
    )
    avatar = models.ImageField(
        upload_to='users/avatar',
        blank=True,
        null=True,
        verbose_name='Аватар',
        help_text='Загрузите аватар пользователя'
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Payments(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        help_text='Выберите пользователя из списка'
    )
    date_payment = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата оплаты',
        help_text='Дата создания платежа'
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Сумма оплаты',
        help_text='Введите сумму оплаты'
    )
    paid_course = models.ForeignKey(
        Course,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Оплаченный курс',
        help_text='Выберите курс из списка'
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Оплаченный урок',
        help_text='Выберите урок из списка'
    )
    payment_method = models.CharField(
        max_length=50,
        verbose_name='Метод оплаты',
        help_text='Выберите метод оплаты'
    )
    session_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='ID сессии',
        help_text='Введите ID сессии платежа'
    )
    link = models.URLField(
        max_length=400,
        blank=True,
        null=True,
        verbose_name='Ссылка на оплату',
        help_text='Введите ссылку на оплату'
    )

    def __str__(self):
        return self.amount

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'
