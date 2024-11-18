from rest_framework import filters
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from users.models import Payments, User
from users.serializers import UserSerializer, PaymentsSerializer
from users.services import convert_rub_to_dollars, create_stripe_price, create_stripe_session

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

class PaymentsCreateAPIView(CreateAPIView):
    serializer = PaymentsSerializer
    queryset = Payments.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        amount_in_dollars = convert_rub_to_dollars(payment.amount)
        price = create_stripe_price(amount_in_dollars)
        session_id, payment_link = create_stripe_session(price)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()