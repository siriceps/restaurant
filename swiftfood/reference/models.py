from django.db import models

from menu.models import Menu
from mycart.models import MyCart


class ReferenceModel(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    order_menu = models.ForeignKey(MyCart, on_delete=models.CASCADE)