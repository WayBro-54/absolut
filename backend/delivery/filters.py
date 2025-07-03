import django_filters
from .models import Delivery


class DeliveryFilter(django_filters.FilterSet):
    date_from = django_filters.DateFilter(
        field_name="created_at", lookup_expr="gte", label="Дата от (YYYY-MM-DD)"
    )
    date_to = django_filters.DateFilter(
        field_name="created_at", lookup_expr="lte", label="Дата до (YYYY-MM-DD)"
    )
    cargo_type = django_filters.CharFilter(
        field_name="cargo_type__code", lookup_expr="exact", label="Тип груза"
    )
    service = django_filters.CharFilter(
        field_name="service__code", lookup_expr="exact", label="Тип доставки"
    )

    class Meta:
        model = Delivery
        fields = ["date_from", "date_to", "cargo_type", "service"]
