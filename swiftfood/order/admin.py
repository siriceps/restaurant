from django.contrib import admin

# Register your models here.
from .models import OrderMenu


@admin.register(OrderMenu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference', 'amount')
