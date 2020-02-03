from django.contrib import admin

# Register your models here.
from .models import Promotions


@admin.register(Promotions)
class PromotionsAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'promotion_name',
            'promotion_code',
            'promotion_picture',
            'description',
            'discount',
    )
