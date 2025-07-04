from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeliveryViewSet

router = DefaultRouter()

router.register(r"delivery", DeliveryViewSet, basename="delivery")

urlpatterns = [
    path("", include(router.urls)),
]
