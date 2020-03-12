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
            'user'
        )

    def get_user(self, menu):
        return SerializerUser(menu.user).data


class SerializerUser(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'categories', 'menu_name', 'price', 'menu_image', 'description', 'material')


class MenuUpdateSerializer(serializers.ModelSerializer):
    # image = ImageField(allow_empty_file=True, allow_null=True, required=False)

    class Meta:
        model = Menu
        fields = ('id', 'categories', 'menu_name', 'price', 'menu_image', 'description', 'material')
