from rest_framework import serializers

from accounts.models import Account
from mycart.models import MyCart


class SerializerUser(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id',
                  'username',
                  'email',
                  )


class MyCartListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = MyCart
        fields = (
            'id',
            'food_menu',
            'user'
        )

    def get_user(self, mycart):
        return SerializerUser(mycart.user).data


class OrderSerializer(serializers.ModelSerializer):
    vat = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = MyCart
        fields = (
            'id',
            'my_cart',
            'quantity',
            'datetime_order',
            'is_paid',
            'service_charge',
            'vat',
            'total',
            'user',
        )

    def get_user(self, mycart):
        return SerializerUser(mycart.user).data

    def get_vat(self):
        vat = 7 / 100
        return vat
