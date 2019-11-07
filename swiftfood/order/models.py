from django.db import models

from restaurant.swiftfood import menu


class OrderMenu(models.Model):
    food_name = models.ForeignKey(menu.menu_name.id, on_delete=models.CASCADE)
    # price = models