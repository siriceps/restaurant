from datetime import datetime
from django.db import models


class Reservation(models.Model):
    amount = models.SmallIntegerField(default=1)
    queue = models.IntegerField(default=1)
    is_confirm = models.BooleanField(default=False)
    datetime = models.DateTimeField(default=datetime.now, blank=True, editable=False)
