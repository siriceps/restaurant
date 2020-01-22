from django.db import models

from swiftfood.menu.models import Menu
from swiftfood.order.models import OrderMenu


class ReferenceModel(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    order_menu = models.ForeignKey(OrderMenu, on_delete=models.CASCADE)