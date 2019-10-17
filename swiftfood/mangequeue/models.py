from django.db import models

from accounts.models import Account


class Queue(models.Model):
    table_number = models.SmallIntegerField(max_length=125, default=0)
    queue = models.SmallIntegerField(max_length=125, default=0)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

