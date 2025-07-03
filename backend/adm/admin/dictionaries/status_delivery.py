from django.contrib import admin

from dictionaries.models import StatusDelivery


@admin.register(StatusDelivery)
class StatusDeliveryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "is_active",
    )
    list_filter = (
        "name",
        "code",
    )
