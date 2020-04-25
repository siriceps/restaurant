from datetime import datetime

from django.conf import settings
from django.db import models

from stock.models import Stock


class Menu(models.Model):
    categories = models.CharField(max_length=50, db_index=True, blank=True)
    menu_name = models.CharField(max_length=50, db_index=True, blank=True)
    price = models.SmallIntegerField(default=0, blank=True)
    menu_image = models.ImageField(upload_to='menu/%Y/%m/', null=True, blank=True)
    discount_price = models.SmallIntegerField(default=0, blank=True)
    description = models.CharField(max_length=50, db_index=True, blank=True)
    is_display = models.BooleanField(default=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    material = models.ForeignKey(Stock, null=True, on_delete=models.CASCADE)
    material_quantity = models.IntegerField(default=0)
    # @staticmethod
    # def is_user_exists(user):
    #     return Menu.objects.filter(user=user).exists()
