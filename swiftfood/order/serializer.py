from django.conf import settings
from rest_framework import serializers

from ice.account.models import Account


class AccountListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = (
            'id',
            'food_name'
        )


