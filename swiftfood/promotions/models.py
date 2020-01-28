from django.db import models

from menu.models import Menu


class Promotion(models.Model):
    promotion_name = models.CharField(max_length=50, db_index=True, blank=True)
    promotion_code = models.CharField(max_length=50, db_index=True, blank=True)
    promotion_picture = models.ImageField(upload_to='promotions/%Y/%m/', null=True, blank=True)
    description = models.CharField(max_length=50, db_index=True, blank=True)
    discount = models.FloatField(default=0)
    food = models.ForeignKey(Menu, on_delete=models.CASCADE)
