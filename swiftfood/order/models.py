from datetime import datetime
from django.db import models

from menu.models import Menu


class OrderMenu(models.Model):
    food_menu = models.ManyToManyField(Menu)
    amount = models.SmallIntegerField(default=1)
    datetime = models.DateTimeField(default=datetime.now, blank=True, editable=False)
    is_confirm = models.BooleanField(default=True)
    service_charge = models.SmallIntegerField(default=0)
    vat = models.FloatField(default=0)
    total = models.FloatField(default=0)

