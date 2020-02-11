from django.conf import settings
from rest_framework import serializers

from order.models import OrderMenu


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderMenu
        fields = (
            'id',
            'material_name',
            'amount_material',
            'material_picture',
        )


