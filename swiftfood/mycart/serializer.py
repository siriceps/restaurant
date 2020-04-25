from rest_framework import serializers

from accounts.models import Account
from menu.models import Menu
from mycart.models import MyCart, Order


class SerializerUser(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id',
            'username',
        )


class SerializerFood(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = (
            'id',
            'menu_name',
            'price',
            'menu_image',
        )


class MyCartListSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    food_menu = serializers.SerializerMethodField()

    class Meta:
        model = MyCart
        fields = (
            'id',
            'food_menu',
            'quantity',
            'datetime_create',
            # 'user',
            # 'order',

        )

    # def get_user(self, mycart):
    #     return SerializerUser(mycart.user).data

    def get_food_menu(self, mycart):
        return SerializerFood(mycart.food_menu).data


class MyCartSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()

    class Meta:
        model = MyCart
        fields = (
            'id',
            'food_menu',
            'quantity',
            'datetime_create',
            # 'user',
            # 'order',

        )

    # def get_user(self, mycart):
    #     return SerializerUser(mycart.user).data
