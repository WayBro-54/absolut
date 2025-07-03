import uuid

from django.utils.translation import gettext_lazy as _
from django.db import models

from dictionaries.models import (
    Service,
    StatusDelivery,
    Transport,
    TypeCargo,
    TypePackaging,
)


class Delivery(models.Model):
    """
    Модель для хранения информации о доставках
    """

    # Основная информация
    tracking_number = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, verbose_name="Трек-номер"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    # Связи с другими моделями
    service = models.ForeignKey(
        Service,
        on_delete=models.PROTECT,
        related_name="deliveries",
        verbose_name="Сервис доставки",
    )
    status = models.ForeignKey(
        StatusDelivery,
        on_delete=models.PROTECT,
        related_name="deliveries",
        verbose_name="Статус доставки",
    )
    transport = models.ForeignKey(
        Transport,
        on_delete=models.PROTECT,
        related_name="deliveries",
        verbose_name="Транспорт",
    )
    cargo_type = models.ForeignKey(
        TypeCargo,
        on_delete=models.PROTECT,
        related_name="deliveries",
        verbose_name="Тип груза",
    )
    packaging_type = models.ForeignKey(
        TypePackaging,
        on_delete=models.PROTECT,
        related_name="deliveries",
        verbose_name="Тип упаковки",
    )

    # Дополнительные поля
    weight = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Вес (кг)"),
        null=True,
        blank=True,
    )
    volume = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Объем (м³)",
        null=True,
        blank=True,
    )
    distance = models.PositiveIntegerField(
        verbose_name="Дистанция (км)", null=True, blank=True
    )
    address_recipient = models.CharField(
        max_length=200,
        verbose_name="Адрес получателя",
        null=True,
        blank=True,
    )
    address_from = models.CharField(
        max_length=200,
        verbose_name="Адрес отправки",
        null=True,
        blank=True,
    )
    notes = models.TextField(blank=True, null=True, verbose_name="Примечания")

    def __str__(self):
        return f"Доставка #{self.tracking_number} ({self.service})"

    class Meta:
        verbose_name = "Доставка"
        verbose_name_plural = "Доставки"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["tracking_number"]),
            models.Index(fields=["status"]),
            models.Index(fields=["created_at"]),
        ]
