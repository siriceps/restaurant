from rest_framework import serializers

from stock.models import Stock


class StockListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = (
            'id',
            'material_name',
            'amount_material',
            # 'material_picture',
        )


