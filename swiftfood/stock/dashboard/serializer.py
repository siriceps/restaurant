from rest_framework import serializers

from stock.models import Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = (
            'id',
            'material_name',
            'quantity_material',
            # 'material_picture',
        )


