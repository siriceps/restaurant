from django.conf import settings
from rest_framework import serializers

from ..models import Account


class AccountListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'image',
            'supervisor',
        )


class AccountCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_null=True, required=False)
    level = serializers.IntegerField(required=False, allow_null=True)

    supervisor = serializers.IntegerField(required=False, allow_null=True)
    department = serializers.IntegerField(required=False, allow_null=True)
    position = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = Account
        fields = (
            'id',
            'email',
            'username',
            'password',
            'first_name',
            'last_name',
            'is_force_reset_password',
            'phone',
            'level',
            'supervisor',
            'department',
            'position',
        )


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(min_length=settings.PASSWORD_MIN)
    is_remember = serializers.BooleanField(default=True)
    language = serializers.CharField(max_length=24, allow_blank=True, required=False, default='en')

    def save(self, **kwargs):
        validated_data = dict(
            list(self.validated_data.items()) + list(kwargs.items())
        )
        return self.create(validated_data)