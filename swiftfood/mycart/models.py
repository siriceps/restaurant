from datetime import datetime
from django.db import models

from accounts.models import Account
from menu.models import Menu
from django.conf import settings


class MyCart(models.Model):
    food_menu = models.ForeignKey(Menu, null=True, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    datetime_create = models.DateTimeField(default=datetime.now, blank=True, editable=False)
    is_order = models.BooleanField(default=False)
    total = models.FloatField(default=0)

    class Meta:
        ordering = ['datetime_create']

    @staticmethod
    def is_user_exists(user):
        return MyCart.objects.filter(user=user).exists()


class Order(models.Model):
    my_cart = models.ManyToManyField(MyCart)
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


class MyCartTest(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    total_price = models.FloatField(default=0)
    datetime_create = models.DateTimeField(default=datetime.now, blank=True, editable=False)
    datetime_update = models.DateTimeField(default=datetime.now, blank=True, editable=False)
    is_confirm = models.BooleanField(default=False)

    @staticmethod
    def is_user_exists(user):
        return Order.objects.filter(user=user).exists()

    def update_total_price(self):
        order_list = OrderTest.objects.filter(my_cart=self)
        total_price = 0
        for order in order_list:
            total_price += order.price
        self.total_price = total_price
        self.save()


class OrderTest(models.Model):
    food_menu = models.ForeignKey(Menu, null=True, on_delete=models.CASCADE)
    my_cart = models.ForeignKey(MyCartTest, null=True, on_delete=models.CASCADE)
    datetime_create = models.DateTimeField(default=datetime.now, blank=True, editable=False)
    quantity = models.IntegerField(default=1)

    @property
    def price(self):
        return self.food_menu.price * self.quantity
