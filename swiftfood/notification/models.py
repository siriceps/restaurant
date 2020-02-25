from django.db import models

from accounts.models import Account


class Notification(models.Model):
    receiver = models.ForeignKey(Account)
    sender = models.ForeignKey(Account)
    message = models.TextField(max_length=64)


