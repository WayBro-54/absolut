from django.contrib import admin

from dictionaries.models import TypeCargo


@admin.register(TypeCargo)
class TypeCargoAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "is_active",
    )
    list_filter = (
        "name",
        "code",
    )
