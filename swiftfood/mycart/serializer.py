from rest_framework import serializers

from accounts.models import Account
from mycart.models import MyCart


class MyCartListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = MyCart
        fields = (
            'id',
            'food_menu',
            'amount',
            'datetime',
            'is_confirm',
            'service_charge',
            'vat',
            'total',
            'user'
        )

    def get_user(self, review):
        return SerializerUser(review.user).data


class SerializerUser(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id',
                  'username',
                  'email',
                  )


class MyCartSerializer(serializers.ModelSerializer):
    vat = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = MyCart
        fields = (
            'id',
            'food_menu',
            'amount',
            'datetime',
            'is_confirm',
            'service_charge',
            'vat',
            'total',
            'user',
        )

    def get_user(self, review):
        return SerializerUser(review.user).data

    def get_vat(self):
        vat = 7 / 100
        return vat
