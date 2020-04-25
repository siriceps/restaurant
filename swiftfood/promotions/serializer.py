from rest_framework import serializers

from menu.models import Menu
from promotions.models import Promotions


class SerializerFood(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = (
            'id',
            'menu_name',
            'price',
            'menu_image',
        )


class PromotionsListSerializer(serializers.ModelSerializer):
    promotion_menu = serializers.SerializerMethodField()

    class Meta:
        model = Promotions
        fields = (
            'id',
            'promotion_name',
            'promotion_code',
            'promotion_picture',
            'description',
            'discount',
            'promotion_menu',
            'datetime_exp'
        )

    def get_promotion_menu(self, promotions):
        return SerializerFood(promotions.promotion_menu).data


class PromotionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotions
        fields = (
            'id',
            'promotion_name',
            'promotion_code',
            'promotion_picture',
            'description',
            'discount',
            'promotion_menu',
            'datetime_exp'
        )
