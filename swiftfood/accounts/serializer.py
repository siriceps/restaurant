import re

from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Account


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
    # notification_count = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            # 'notification_count'
        )


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(min_length=settings.PASSWORD_MIN)
    is_remember = serializers.BooleanField(default=True)
    language = serializers.CharField(max_length=24, allow_blank=True, required=False, default='en')

    # def send_reset_password(self, account):
    #     token = account.force_reset_password()
    #     email = account.email
    #     site_url = Config.pull_value('config-site-url')
    #     ForgetPasswordUser.create_forget_user_password(email, token, site_url, method=2)
    #     return token
    #
    # def validate_password(self, value):
    #     if len(value) < settings.PASSWORD_MIN:
    #         raise ValidationError('Language not in Config')
    #     else:
    #         return value
    #
    # def validate_username(self, value):
    #     key_login = Config.pull_value('account-login-key')
    #     if 'email' in key_login and 'or' not in key_login:
    #         if not check_email(value):
    #             raise ValidationError('Not Email Format')
    #     return value


class RegisterSerializer(LoginSerializer):
    confirm_password = serializers.CharField(min_length=settings.PASSWORD_MIN)
    email = serializers.CharField(max_length=255)
    title = serializers.CharField(max_length=255, required=False, allow_blank=True)
    first_name = serializers.CharField(max_length=120, required=False, allow_blank=True)
    last_name = serializers.CharField(max_length=120, required=False, allow_blank=True)
    is_subscribe = serializers.BooleanField(default=True, required=False)
    is_term_and_condition = serializers.BooleanField(default=True, required=False)