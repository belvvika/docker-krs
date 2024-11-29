from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from celery import shared_task

@shared_task
def send_information_about_update(email):
    send_mail('Курс обновлен!', 'Курс, на который вы подписаны, был обновлен. Посмотрите изменения.', EMAIL_HOST_USER, [email])
