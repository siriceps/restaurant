from rest_framework import serializers

from .models import ReferenceModel


class ReferenceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceModel
        fields = (
            'id',
            'menu',
            'order_menu',
        )

