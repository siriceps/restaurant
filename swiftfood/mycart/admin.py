from django.contrib import admin

# Register your models here.
from .models import MyCart


@admin.register(MyCart)
class MyCartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'quantity',
        'datetime',
        'is_confirm',
        'service_charge',
        'vat',
        'total',
        'user',
        'is_paid',
    )
