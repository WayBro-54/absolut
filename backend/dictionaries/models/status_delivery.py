from django.utils.translation import gettext_lazy as _
from django.db import models


class StatusDelivery(models.Model):
    name = models.CharField(_("Статус доставки"), max_length=255)
    code = models.CharField(_("Код статуса"), max_length=255, unique=True)
    is_active = models.BooleanField(_("Активна"), default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Status Delivery")
        verbose_name_plural = _("Status Deliveries")
