from datetime import datetime
from django.db import models


class Reservation(models.Model):
    quantity = models.SmallIntegerField(default=1)
    queue = models.IntegerField(default=1,)
    is_confirm = models.BooleanField(default=False)
    datetime = models.DateTimeField(default=datetime.now, blank=True, editable=False)
    count = models.SmallIntegerField(default=1)  # for call queue
