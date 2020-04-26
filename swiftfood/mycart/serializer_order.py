from rest_framework import serializers

from accounts.models import Account
from mycart.models import Order, MyCart


class SerializerUser(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id',
            'username',
        )


class OrderListSerializer(serializers.ModelSerializer):
    # vat = serializers.SerializerMethodField()
    # user = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'id',
            'my_cart',
            'datetime_order',
            'is_paid',
            'service_charge',
            'vat',
            'total',
            # 'user',
        )

    # def get_user(self, order):
    #     return SerializerUser(order.user).data

    # def get_vat(self):
    #     vat = 7 / 100
    #     return vat


class OrderCreateSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    # service_charge = serializers.SerializerMethodField()
    # vat = serializers.SerializerMethodField()
    my_cart = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'id',
            'my_cart',
            'datetime_order',
            'service_charge',
            'vat',
            'total',
            # 'user',
        )

    def get_my_cart(self):
        return MyCart.objects.filter(
            is_order=False,
        )
    # def get_user(self, order):
    #     return SerializerUser(order.user).data

    # def get_vat(self):
    #     vat = 7 / 100
    #     return vat

    #
    # def get_total(self):
    #     return None
    #
    # def get_service_charge(self):
    #     service_charge = 10 / 100
    #     return service_charge
