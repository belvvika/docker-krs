from django.core.management import BaseCommand

from materials.models import Course
from users.models import User, Payments
class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email='admin@example.com')
        user.set_password('123456')
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

        payment_1 = {
            'user': user,
            'amount': 1000,
            'payment_method': 'Оплата картой',
            'paid_course': Course.objects.get(pk=1),
            'paid_lesson': None
        }
        payment_2 = {
            'user': user,
            'amount': 500,
            'payment_method': 'Оплата PayPal',
            'paid_course': Course.objects.get(pk=1),
            'paid_lesson': Course.objects.get(pk=1)
        }
        payment_3 = {
            'user': user,
            'amount': 200,
            'payment_method': 'Оплата наличными',
            'paid_course': Course.objects.get(pk=1),
            'paid_lesson': Course.objects.get(pk=2)
        }
        [Payments.objects.create(**payment) for payment in (payment_1, payment_2, payment_3)]
        print('Payments created')