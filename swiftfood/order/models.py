from django.db import models

from menu.models import Menu
# from reference.models import ReferenceModel


class OrderMenu(models.Model):
    food_menu = models.ManyToManyField(Menu)
    amount = models.SmallIntegerField(default=1)


