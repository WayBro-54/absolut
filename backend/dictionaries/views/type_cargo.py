from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from dictionaries.models import TypeCargo
from dictionaries.serializers import TypeCargoSerializer


class TypeCargoListAPIView(ReadOnlyModelViewSet):
    queryset = TypeCargo.objects.all()
    serializer_class = TypeCargoSerializer
    # permission_classes = (IsAuthenticated,)
