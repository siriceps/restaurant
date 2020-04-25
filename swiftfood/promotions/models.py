from datetime import datetime

from django.db import models

from menu.models import Menu
from mycart.models import MyCart


class Promotions(models.Model):
    promotion_name = models.CharField(max_length=50, db_index=True, blank=True)
    promotion_code = models.CharField(max_length=50, db_index=True, blank=True)
    promotion_picture = models.ImageField(upload_to='promotions/%Y/%m/', null=True, blank=True)
    description = models.CharField(max_length=50, db_index=True, blank=True)
    discount = models.FloatField(default=0)
    promotion_menu = models.ForeignKey(Menu, null=True, on_delete=models.CASCADE)
    datetime_exp = models.DateTimeField(default=datetime.now, blank=True, editable=False)