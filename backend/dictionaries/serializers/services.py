from rest_framework import serializers

from dictionaries.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            "name",
            "code",
        )
