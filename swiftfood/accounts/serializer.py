# from rest_framework.fields import ImageField

from rest_framework import serializers

from swiftfood import settings
from .models import Account


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(allow_blank=False, required=True)
    password = serializers.CharField(style={'input_type': 'password'}, max_length=20, min_length=2)


class AccountProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'point']


class ProfileUpdateSerializer(serializers.ModelSerializer):
    # image = ImageField(allow_empty_file=True, allow_null=True, required=False)

    class Meta:
        model = Account
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'point', 'image')


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(allow_blank=False, required=True)
    password = serializers.CharField(min_length=settings.PASSWORD_MIN)
    confirm_password = serializers.CharField(min_length=settings.PASSWORD_MIN, required=False)
    email = serializers.CharField(max_length=255, required=True, allow_blank=False)
    first_name = serializers.CharField(max_length=120, required=True, allow_blank=False)
    last_name = serializers.CharField(max_length=120, required=True, allow_blank=False)
    phone = serializers.CharField(max_length=10, required=True, allow_blank=False)

    class Meta:
        model = Account
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            # 'image',
            'password',
            'confirm_password'
        )

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(allow_blank=False, required=True)
    new_password = serializers.CharField(allow_blank=False, required=True, min_length=settings.PASSWORD_MIN)
    confirm_password = serializers.CharField(allow_blank=False, required=True, min_length=settings.PASSWORD_MIN)


class ForgetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class AccountListSerializer(serializers.Serializer):
    username = serializers.CharField(allow_blank=False, required=True)
    email = serializers.CharField(max_length=255, required=True, allow_blank=False)
    first_name = serializers.CharField(max_length=120, required=True, allow_blank=False)
    last_name = serializers.CharField(max_length=120, required=True, allow_blank=False)
    phone = serializers.CharField(max_length=10, required=True, allow_blank=False)


class AccountRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'phone']


class NoneSerializer(serializers.Serializer):
    pass


class RegisterStaffSerializer(serializers.ModelSerializer):
    username = serializers.CharField(allow_blank=False, required=True)
    password = serializers.CharField(min_length=settings.PASSWORD_MIN)
    confirm_password = serializers.CharField(min_length=settings.PASSWORD_MIN, required=False)
    email = serializers.CharField(max_length=255, required=True, allow_blank=False)
    first_name = serializers.CharField(max_length=120, required=True, allow_blank=False)
    last_name = serializers.CharField(max_length=120, required=True, allow_blank=False)
    phone = serializers.CharField(max_length=10, required=True, allow_blank=False)
    is_staff = serializers.BooleanField(default=True)
    is_admin = serializers.BooleanField(default=True)

    class Meta:
        model = Account
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            # 'image',
            'is_staff',
            'is_admin',
            'password',
            'confirm_password'
        )


class StaffListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'is_staff', 'is_admin']
