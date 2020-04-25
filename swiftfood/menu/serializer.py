from rest_framework import serializers

from accounts.models import Account
from stock.models import Stock
from .models import Menu


class SerializerUser(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username')


class MenuListSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    material = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = (
            'id',
            'categories',
            'menu_name',
            'price',
            'menu_image',
            'discount_price',
            'description',
            'material',
            'is_display',
            # 'user'
        )

    def get_material(self, menu):
        return SerializerStock(menu.material).data


class CategorySerializer(serializers.ModelSerializer):
    material = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ('id', 'categories', 'menu_name', 'price', 'menu_image', 'description', 'material')

    def get_material(self, menu):
        return SerializerStock(menu.material).data


class MenuUpdateSerializer(serializers.ModelSerializer):
    material = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ('id', 'categories', 'menu_name', 'price', 'menu_image', 'description', 'material')

    def get_material(self, menu):
        return SerializerStock(menu.material).data


class SerializerStock(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = (
            'id',
            'material_name',
            'quantity_material',
            'material_picture',
        )
