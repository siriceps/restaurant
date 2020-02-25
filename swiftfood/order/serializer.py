from rest_framework import serializers

from order.models import OrderMenu


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderMenu
        fields = (
            'id',
            'food_menu',
            'amount',
            'datetime',
            'is_confirm',
            'service_charge',
            'vat',
            'total',
            # 'price'
        )


class OrderSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = OrderMenu
        fields = (
            'id',
            'food_menu',
            'amount',
            'datetime',
            'is_confirm',
            'service_charge',
            'vat',
            'total',
        )
    # def get_total(self,total):
    #     get_food_menu(total)
