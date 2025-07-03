from django.contrib import admin

from dictionaries.models import TypePackaging


@admin.register(TypePackaging)
class TypePackagingAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "is_active",
    )
    list_filter = (
        "name",
        "code",
    )
