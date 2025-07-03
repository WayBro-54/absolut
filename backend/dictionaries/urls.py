from django.urls import path, include
from rest_framework import routers
from .views import TypeCargoListAPIView, ServiceListAPIView

router = routers.DefaultRouter()
router.register(r"types-cargo", TypeCargoListAPIView, basename="types-cargo")
router.register(r"services", ServiceListAPIView, basename="services")

urlpatterns = [
    path("dictionaries/", include(router.urls)),
]
