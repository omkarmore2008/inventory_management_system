from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from inventory_management_system.inventory.api.views import InventorryViewSet
from inventory_management_system.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("items", InventorryViewSet)


app_name = "api"
urlpatterns = router.urls
