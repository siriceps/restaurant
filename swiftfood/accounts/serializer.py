from datetime import timezone

from swiftfood import settings
from rest_framework import serializers

from .models import Account


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(allow_blank=False, required=True)
    password = serializers.CharField(style={'input_type': 'password'}, max_length=20, min_length=2)


class AccountRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class LoginModel(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'first_name', 'last_name', 'email']


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(allow_blank=False, required=True)
    password = serializers.CharField(min_length=settings.PASSWORD_MIN)
    confirm_password = serializers.CharField(min_length=settings.PASSWORD_MIN, required=False)
    email = serializers.CharField(max_length=255, required=True, allow_blank=False)
    first_name = serializers.CharField(max_length=120, required=True, allow_blank=False)
    last_name = serializers.CharField(max_length=120, required=True, allow_blank=False)
    phone = serializers.CharField(max_length=10, required=True, allow_blank=False)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(allow_blank=False, required=True)
    new_password = serializers.CharField(allow_blank=False, required=True, min_length=settings.PASSWORD_MIN)
    confirm_password = serializers.CharField(allow_blank=False, required=True, min_length=settings.PASSWORD_MIN)


class ForgetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()