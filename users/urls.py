from django.urls import path
from rest_framework.routers import SimpleRouter

from users.views import PaymentsViewSet
from users.apps import UsersConfig

app_name = UsersConfig.name

router = SimpleRouter()
router.register('', PaymentsViewSet)

urlpatterns = []

urlpatterns += router.urls