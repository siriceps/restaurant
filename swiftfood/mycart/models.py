from datetime import datetime
from django.db import models

from accounts.models import Account
from menu.models import Menu
from django.conf import settings


class Order(models.Model):
    # my_cart = models.ForeignKey(MyCart, on_delete=models.CASCADE)
    datetime_order = models.DateTimeField(default=datetime.now, blank=True, editable=False)
    service_charge = models.FloatField(default=0)
    vat = models.FloatField(default=0)
    total = models.FloatField(default=0)
    is_paid = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-datetime_order']

    @staticmethod
    def is_user_exists(user):
        return Order.objects.filter(user=user).exists()

    @staticmethod
    def pull(id):
        try:
            order = Order.objects.get(id=id)
        except:
            order = None
        return order

    # def get_mycart_list(self):
    #     return self.mycart_set.all()


class MyCart(models.Model):
    food_menu = models.ForeignKey(Menu, null=True, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

    # order = models.ForeignKey(Order, on_delete=models.CASCADE)
    datetime_create = models.DateTimeField(default=datetime.now, blank=True, editable=False)

    class Meta:
        ordering = ['datetime_create']

    @staticmethod
    def is_user_exists(user):
        return MyCart.objects.filter(user=user).exists()

    @staticmethod
    def pull(id):
        try:
            my_cart = MyCart.objects.get(id=id)
        except:
            my_cart = None
        return my_cart

    # def get_order_list(self):
    #     return self.order_set.all()
    # @property
    # def get_food_menu(self):
    #     total = 0
    #     for i in self.food_menu:
    #         total += i.price
    #     return total
