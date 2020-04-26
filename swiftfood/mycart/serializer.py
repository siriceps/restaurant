from django.db.models import Sum
from rest_framework import serializers

from accounts.models import Account
from menu.models import Menu
from mycart.models import MyCart, OrderTest, MyCartTest


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

        )

    # def get_user(self, mycart):
    #     return SerializerUser(mycart.user).data


class MyCartTestSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = MyCartTest
        fields = (
            'id',
            'total_price',
        )

    def get_total_price(self, mycarttest):
        return mycarttest.total_price * 1.07


class OrderTestSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    food_name = serializers.SerializerMethodField()

    class Meta:
        model = OrderTest
        fields = (
            'id',
            'food_name',
            'quantity',
            'price',
        )

    def get_food_name(self, ordertest):
        return ordertest.food_menu.menu_name


class OrderTestCreateSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()

    class Meta:
        model = OrderTest
        fields = (
            'food_menu',
            'quantity',
        )


class MyCartTestOrderSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    order_list = serializers.SerializerMethodField()
    count_order = serializers.SerializerMethodField()

    class Meta:
        model = MyCartTest
        fields = (
            'id',
            'total_price',
            'order_list',
            'count_order',
        )

    def get_order_list(self, mycarttest):
        order = OrderTest.objects.filter(my_cart=mycarttest)
        return OrderTestSerializer(order, many=True).data

    def get_total_price(self, mycarttest):
        return mycarttest.total_price * 1.07

    def get_count_order(self, mycarttest):
        return OrderTest.objects.filter(my_cart=mycarttest).aggregate(Sum('quantity'))['quantity__sum']
