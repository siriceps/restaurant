from django.conf import settings
from rest_framework import serializers

from order.models import OrderMenu


class OrderListSerializer(serializers.ModelSerializer):

    # food_name = serializers. models
    # categories =
    # price =
    class Meta:
        model = OrderMenu
        fields = (
            'id',
            'food_menu',
            'amount',
            # 'price',
            # 'categories'
        )


