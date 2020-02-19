
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import PermissionsMixin, User
from django.contrib.auth.validators import UnicodeUsernameValidator, ASCIIUsernameValidator
from django.db import models
from django.utils import six
from django.utils.translation import ugettext_lazy as _


def generate_username():
    import random
    import string
    return ''.join(random.sample(string.ascii_lowercase, 6))


class AccountManager(BaseUserManager):

    def create_user(self, username, password):
        if username is None:
            raise ValueError('The given username must be set')

        user = self.model(
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """

        user = self.create_user(username, password)
        user.is_admin = True
        user.is_superuser = True
        user.type = 1
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    # TYPE = (
    #     (0, 'super admin'),
    #     (1, 'admin'),
    #     (2, 'staff'),
    #     (3, 'user'),
    # )

    first_name = models.CharField(max_length=120, db_index=True, blank=True)
    last_name = models.CharField(max_length=120, db_index=True, blank=True)
    phone = models.CharField(max_length=64, null=True, blank=True, db_index=True)
    image = models.ImageField(upload_to='accounts/%Y/%m/', null=True, blank=True)
    code = models.CharField(max_length=32, db_index=True, blank=True, null=True, default=None)  # Employee id
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    # position = models.IntegerField(choices=, default=3)
    username_validator = UnicodeUsernameValidator() if six.PY3 else ASCIIUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    email = models.EmailField(
        verbose_name='Email address',
        max_length=255,
        db_index=True,
        null=True,
        blank=True
    )

    token = models.CharField(max_length=32, null=True, blank=True, db_index=True)
    facebook_user_id = models.CharField(max_length=255, blank=True)
    google_user_id = models.CharField(max_length=255, blank=True)
    point = models.SmallIntegerField(default=0)

    objects = AccountManager()
    USERNAME_FIELD = 'username'

    class Meta:
        ordering = ['username']


class PasswordHistory(models.Model):
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    password = models.CharField(_('password'), max_length=128)
    datetime_create = models.DateTimeField(auto_now_add=True, db_index=True)

    @staticmethod
    def check_password(account, password, old_password):
        def setter(password):
            account.set_password(password)
            # Password hash upgrades shouldn't be considered password changes.
            account._password = None
            account.save(update_fields=['password'])

        return check_password(password, old_password, setter)


class ForgetPassword(models.Model):
    token = models.CharField(max_length=64)
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

# class CustomUser(AbstractUser):