from django.contrib import admin

from dictionaries.models import Transport


@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "is_active",
    )
    list_filter = (
        "name",
        "code",
    )
