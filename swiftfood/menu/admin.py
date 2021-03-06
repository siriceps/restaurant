from django.contrib import admin

from .models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'categories',
        'menu_name',
        'price',
        'menu_image',
        'discount_price',
        'description',
        'is_display',
        'material_quantity',
    )
