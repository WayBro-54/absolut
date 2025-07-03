from rest_framework import serializers
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={"input_type": "password"})

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("Пользователь неактивен.")
                data["user"] = user
            else:
                raise serializers.ValidationError("Неверный логин или пароль.")
        else:
            raise serializers.ValidationError("Укажите username и пароль.")
        return data
