from datetime import datetime
from django.db import models

from django.conf import settings

from accounts.models import Account


class Reservation(models.Model):
    quantity = models.SmallIntegerField(default=1)
    queue = models.IntegerField(default=1, )
    is_confirm = models.BooleanField(default=False)
    datetime = models.DateTimeField(default=datetime.now, blank=True, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

    @staticmethod
    def is_user_exists(user):
        return Reservation.objects.filter(user=user).exists()

    @staticmethod
    def count():
        return Reservation.objects.count()
