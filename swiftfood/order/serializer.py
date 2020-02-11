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

        )
