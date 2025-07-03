from rest_framework import serializers

from dictionaries.models import TypeCargo


class TypeCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeCargo
        fields = (
            "name",
            "code",
        )
