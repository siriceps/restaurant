from rest_framework import serializers

from ..models import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = (
            'id',
            'categories',
            'menu_name',
            'price',
            # 'menu_image',
            'discount_price',
            'description',
            # 'date_exp',
            # 'material',
        )