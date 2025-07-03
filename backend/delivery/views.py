import uuid
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Delivery
from .serializers import DeliverySerializer, DeliveryWriteSerializer
from .filters import DeliveryFilter


class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.select_related(
        "service", "status", "transport", "cargo_type", "packaging_type"
    ).order_by("-created_at")
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DeliveryFilter
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DeliveryWriteSerializer
        return DeliverySerializer

    def perform_create(self, serializer):
        serializer.save(tracking_number=uuid.uuid4())
