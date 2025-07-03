from django.utils.translation import gettext_lazy as _
from django.db import models


class Service(models.Model):
    name = models.CharField(
        _("Имя услуги"),
        max_length=255,
    )
    code = models.CharField(_("Код услуги"), max_length=255, unique=True)
    is_active = models.BooleanField(_("Активна"), default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")
        ordering = ["name"]
