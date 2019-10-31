from django.db import models


class OrderMenu(models.Model):
    food_name = models.ForeignKey(null=True)
    food_amount = models.SmallIntegerField(default=0, null=True)
    price = models.SmallIntegerField()
