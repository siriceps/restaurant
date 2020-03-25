from django.conf import settings
from rest_framework import serializers

from mycart.models import MyCart


# class OrderListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MyCart
#         fields = (
#             'id',
#             'food_menu',
#             'quantity',
#             'datetime',
#             'is_confirm',
#             'service_charge',
#             'vat',
#             'total',
#             'user',
#             'is_paid',
#         )


