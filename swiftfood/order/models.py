from django.db import models

from swiftfood.menu.models import Menu
from swiftfood.reference.models import ReferenceModel


class OrderMenu(models.Model):
    reference = models.ForeignKey(ReferenceModel, on_delete=models.CASCADE)
    amount = models.SmallIntegerField(default=1, max_length=30)


# @staticmethod
#     def pull_menu(id):
#         menu = Menu.objects.filter(id=id).first()
#         if menu is None:
#             provider = Menu.objects.create(name=name)
#         return provider