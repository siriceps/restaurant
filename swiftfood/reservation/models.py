from django.db import models


class Reservation(models.Model):
    amount = models.SmallIntegerField(default=1)
    queue = models.IntegerField(default=1)
