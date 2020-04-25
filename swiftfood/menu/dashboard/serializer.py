from rest_framework import serializers

from accounts.models import Account
from ..models import Menu
from ..serializer import SerializerStock


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
            'material',
        )


class MenuUpdateSerializerAdmin(serializers.ModelSerializer):
    material = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ('id', 'categories', 'menu_name', 'price', 'menu_image', 'description', 'material')

    def get_material(self, menu):
        return SerializerStock(menu.material).data


class MenuCreateSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'categories', 'menu_name', 'price', 'description', 'material')
