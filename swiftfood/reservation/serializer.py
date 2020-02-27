from rest_framework import serializers

from reservation.models import Reservation


class ReservationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            'id',
            'quantity',
            'queue',
            'datetime',
            'is_confirm',
            'count',
        )


class ReservationDestroy(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            'count',
        )
