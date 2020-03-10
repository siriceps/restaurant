from django.conf import settings
from rest_framework import serializers

from accounts.models import Account
from .models import Menu


class MenuListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = (
            'id',
            'categories',
            'menu_name',
            'price',
            'menu_image',
            'discount_price',
            'description',
            'material',
            'is_display',
        )

    def get_user(self, Menu):
        return SerializerUser(Menu.user).data


class SerializerUser(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id',
                  'username',
                  )
