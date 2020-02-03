from django.contrib import admin

# Register your models here.
from .models import OrderMenu


@admin.register(OrderMenu)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount')