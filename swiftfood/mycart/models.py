from datetime import datetime
from django.db import models

from accounts.models import Account
from menu.models import Menu
from django.conf import settings


class MyCart(models.Model):
    food_menu = models.ManyToManyField(Menu)
    quantity = models.SmallIntegerField(default=1)
    datetime = models.DateTimeField(default=datetime.now, blank=True, editable=False)
    is_confirm = models.BooleanField(default=True)
    service_charge = models.SmallIntegerField(default=0)
    vat = models.FloatField(default=0)
    total = models.FloatField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)

    @staticmethod
    def is_user_exists(user):
        return MyCart.objects.filter(user=user).exists()

    @property
    def get_food_menu(self):
        total = 0
        for i in self.food_menu:
            total += i.price
        return total
