from datetime import timezone

from swiftfood import settings
from rest_framework import serializers


from .models import Account


class LoginModel(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = {'username', 'password'}


class RegisterModel(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = {'username', 'password', 'first_name', 'last_name', 'email', 'phone', }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(allow_blank=False, required=True)
    password = serializers.CharField(style={'input_type': 'password'}, max_length=20)


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(min_length=settings.PASSWORD_MIN)
    confirm_password = serializers.CharField(min_length=settings.PASSWORD_MIN)
    email = serializers.CharField(max_length=255, required=True, allow_blank=False)
    first_name = serializers.CharField(max_length=120, required=True, allow_blank=False)
    last_name = serializers.CharField(max_length=120, required=True, allow_blank=False)
    phone = serializers.CharField(max_length=10, required=True, allow_blank=False)
