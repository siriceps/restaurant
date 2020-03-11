from django.contrib import admin

# Register your models here.
from .models import MyCart, Order


@admin.register(MyCart)
class MyCartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'quantity',
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
