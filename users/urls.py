from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import PaymentsViewSet, UserCreateAPIView, PaymentsCreateAPIView
from users.apps import UsersConfig

app_name = UsersConfig.name

router = SimpleRouter()
router.register('', PaymentsViewSet)

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(permission_classes=AllowAny,), name='register'),
    path('login', TokenObtainPairView.as_view(permission_classes=AllowAny,), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('payments/', PaymentsCreateAPIView.as_view(), name='payments'),
]

urlpatterns += router.urls