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


