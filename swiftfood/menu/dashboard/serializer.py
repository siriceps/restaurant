from rest_framework import serializers

from accounts.models import Account
from ..models import Menu


class MenuSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = (
            'id',
            'categories',
            'menu_name',
            'price',
            # 'menu_image',
            'discount_price',
            'description',
            'material',
            'user'
        )

    def get_user(self, menu):
        return SerializerUser(menu.user).data


class SerializerUser(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id',
                  'username',
                  )


class MenuUpdateSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'categories', 'menu_name', 'price', 'menu_image', 'description', 'material')


class MenuCreateSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'categories', 'menu_name', 'price', 'description', 'material')
