from django.conf import settings
from rest_framework import serializers

from order.models import OrderMenu
from promotions.models import Promotions


class PromotionsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promotions
        fields = (
            'id',
            'food_menu',
            'promotion_name',
            # 'promotion_code',
            'promotion_picture',
            'description',
            'discount',
        )


class PromotionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotions
        fields = (
            'id',
            'food_menu',
            'promotion_name',
            'promotion_code',
            'promotion_picture',
            'description',
            'discount',
        )

