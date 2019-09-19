import re

from django.conf import settings
from rest_framework import serializers

from swiftfood.account.models import Account


def check_email(value):
    if re.compile('[^@]+@[^@]+\.[^@]+').search(value):
        return True
    else:
        return False


def check_password(value):
    if re.compile('(?=.{8,})(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+|~=`{}:;<>?,.])').match(value):
        return True
    else:
        return False


class AccountSerializer(serializers.ModelSerializer):
    notification_count = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'notification_count'
        )


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(min_length=settings.PASSWORD_MIN)
    is_remember = serializers.BooleanField(default=True)
    language = serializers.CharField(max_length=24, allow_blank=True, required=False, default='en')
