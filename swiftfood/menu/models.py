from django.db import models


class Menu(models.Model):
    categories = models.CharField(max_length=50, db_index=True, blank=True)
    menu_name = models.CharField(max_length=50, db_index=True, blank=True)
    price = models.SmallIntegerField(default=0, blank=True)
    menu_image = models.ImageField(upload_to='menu/%Y/%m/', null=True, blank=True)