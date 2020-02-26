from rest_framework import serializers

from promotions.models import Promotions


class PromotionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotions
        fields = (
            'id',
            'promotion_name',
            # 'promotion_code',
            'promotion_picture',
            'description',
            'discount',
            'promotion_order',
            'datetime_exp'
        )
