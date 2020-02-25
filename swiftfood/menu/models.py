from datetime import datetime

from django.db import models

from stock.models import Stock


class Menu(models.Model):
    categories = models.CharField(max_length=50, db_index=True, blank=True)
    menu_name = models.CharField(max_length=50, db_index=True, blank=True)
    price = models.SmallIntegerField(default=0, blank=True)
    menu_image = models.ImageField(upload_to='menu/%Y/%m/', null=True, blank=True)
    discount_price = models.SmallIntegerField(default=0, blank=True)
    description = models.CharField(max_length=50, db_index=True, blank=True)
    date_exp = models.DateTimeField(default=datetime.now, blank=True, editable=False)

