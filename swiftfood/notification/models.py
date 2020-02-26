from django.db import models

from accounts.models import Account


class Notification(models.Model):
    # receiver = models.ForeignKey(Account, on_delete=models.CASCADE)
    # sender = models.ForeignKey(Account, on_delete=models.CASCADE)
    message = models.TextField(max_length=64)
