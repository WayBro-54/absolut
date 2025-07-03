from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from delivery.models import Delivery
from dictionaries.models import (
    Service,
    StatusDelivery,
    Transport,
    TypeCargo,
    TypePackaging,
)


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["name", "code"]


class StatusDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusDelivery
        fields = ["id", "name", "code"]


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = ["id", "name", "code"]


class TypeCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeCargo
        fields = ["name", "code"]


class TypePackagingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypePackaging
        fields = ["id", "name", "code"]


class DeliverySerializer(serializers.ModelSerializer):
    """сериализатор для чтения"""

    tracking_number = serializers.UUIDField(read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    service = ServiceSerializer(help_text="Услуга")
    status = StatusDeliverySerializer()
    transport = TransportSerializer()
    cargo_type = TypeCargoSerializer()
    packaging_type = TypePackagingSerializer()
    weight = serializers.DecimalField(max_digits=10, decimal_places=2)
    volume = serializers.DecimalField(max_digits=10, decimal_places=2)
    distance = serializers.IntegerField(min_value=1, allow_null=True, required=False)
    notes = serializers.CharField(allow_blank=True, required=False)
    address_recipient = serializers.CharField()
    address_from = serializers.CharField()

    class Meta:
        model = Delivery
        fields = [
            "id",
            "tracking_number",
            "created_at",
            "updated_at",
            "service",
            "status",
            "transport",
            "cargo_type",
            "packaging_type",
            "weight",
            "volume",
            "distance",
            "notes",
            "address_recipient",
            "address_from",
        ]
        read_only_fields = ["id", "tracking_number", "created_at", "updated_at"]


class DeliveryWriteSerializer(serializers.ModelSerializer):
    """Сериализатор для создания и обновления"""

    # за место <model>.objects.all(), конечно, лучше использовать DAO, тут маленький проект.
    service = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.all(), label=_("Имя услуги")
    )
    status = serializers.PrimaryKeyRelatedField(
        queryset=StatusDelivery.objects.all(), label=_("Статус заявки")
    )
    transport = serializers.PrimaryKeyRelatedField(
        queryset=Transport.objects.all(), label=_("Номер машины")
    )
    cargo_type = serializers.PrimaryKeyRelatedField(
        queryset=TypeCargo.objects.all(), label=_("Тип груза")
    )
    packaging_type = serializers.PrimaryKeyRelatedField(
        queryset=TypePackaging.objects.all(), label=_("Тип упаковки")
    )

    class Meta:
        model = Delivery
        fields = [
            "service",
            "status",
            "transport",
            "cargo_type",
            "packaging_type",
            "weight",
            "volume",
            "distance",
            "notes",
            "address_recipient",
            "address_from",
        ]

    def validate(self, attrs):
        if not attrs.get("address_recipient"):
            raise serializers.ValidationError(
                _('fields "address_recipient" is required.')
            )
        if not attrs.get("address_from"):
            raise serializers.ValidationError(_('fields "address_from" is required.'))
        if not attrs.get("distance"):
            raise serializers.ValidationError(_('fields "distance" is required.'))
        return attrs
