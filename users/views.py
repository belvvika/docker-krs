from rest_framework import filters

from rest_framework.viewsets import ModelViewSet

from users.models import Payments

class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ('date_payment')
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')