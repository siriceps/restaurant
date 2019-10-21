from django.conf import settings
from rest_framework import serializers

from ..models import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = (
            'id',
            'categories',
            'menu_name',
            'price',
            'menu_image',
        )

