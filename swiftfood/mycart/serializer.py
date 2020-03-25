from rest_framework import serializers

from accounts.models import Account
from mycart.models import MyCart, Order


class SerializerUser(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id',
            'username',
        )


class MyCartListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = MyCart
        fields = (
            'id',
            'food_menu',
            'quantity',
            'datetime_create',
            'user',
            # 'order',

        )

    def get_user(self, mycart):
        return SerializerUser(mycart.user).data


class OrderListSerializer(serializers.ModelSerializer):
    vat = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    mycart_list = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'id',
            # 'my_cart',
            'datetime_order',
            'is_paid',
            'service_charge',
            'vat',
            'total',
            'user',
            'mycart_list',
        )

    def get_user(self, order):
        return SerializerUser(order.user).data

    def get_vat(self):
        vat = 7 / 100
        return vat

    def get_mycart_list(self, order):
        return MyCartListSerializer(order.get_mycart_list(), many=True).data


class OrderCreateSerializer(serializers.ModelSerializer):
    vat = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()
    service_charge = serializers.SerializerMethodField()
    is_paid = serializers.BooleanField(default=False)

    class Meta:
        model = Order
        fields = (
            'id',
            'datetime_order',
            'is_paid',
            'service_charge',
            'vat',
            'total',
            'user',

        )

    def get_user(self, order):
        return SerializerUser(order.user).data

    def get_vat(self):
        vat = 7 / 100
        return vat

    def get_total(self):
        return None

    def get_service_charge(self):
        service_charge = 10 / 100
        return service_charge
