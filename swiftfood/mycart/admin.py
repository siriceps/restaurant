from django.contrib import admin

# Register your models here.
from .models import MyCart, Order, OrderTest, MyCartTest


@admin.register(MyCart)
class MyCartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'food_menu',
        'quantity',
        'datetime_create',
        'user',
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'datetime_order',
        'is_paid',
        'service_charge',
        'vat',
        'total',
        'user',
    )


@admin.register(OrderTest)
class OrderTestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'food_menu',
        'my_cart',
        'datetime_create',
        'quantity',
    )


@admin.register(MyCartTest)
class MyCartTestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'total_price',
        'datetime_create',
        'datetime_update',
        'is_confirm',
    )
