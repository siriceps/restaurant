from django.contrib import admin

from restaurant.swiftfood.menu.models import Menu


@admin.register(Menu)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('categories', 'menu_name', 'price', 'menu_image')

