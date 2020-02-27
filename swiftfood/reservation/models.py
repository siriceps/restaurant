from datetime import datetime
from django.db import models

from django.conf import settings


class Reservation(models.Model):
    quantity = models.SmallIntegerField(default=1)
    queue = models.IntegerField(default=1, )
    is_confirm = models.BooleanField(default=False)
    datetime = models.DateTimeField(default=datetime.now, blank=True, editable=False)
    count = models.SmallIntegerField(default=1)  # for call queue
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)


