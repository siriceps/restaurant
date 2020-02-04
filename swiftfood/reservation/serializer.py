from rest_framework import serializers

from reservation.models import Reservation


class ReservationListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = (
            'id',
            'amount',
            'queue',
        )



