from rest_framework import serializers

from promotions.generator_code import gen_code
from promotions.models import Promotions


class PromotionsSerializer(serializers.ModelSerializer):
    # promotion_code = serializers.SerializerMethodField()

    class Meta:
        model = Promotions
        fields = (
            'id',
            'promotion_name',
            'promotion_code',
            # 'promotion_picture',
            'description',
            'discount',
            # 'promotion_order',
        )

    # def get_promotion_code(self):
    #     code = gen_code(16)
    #     return code
