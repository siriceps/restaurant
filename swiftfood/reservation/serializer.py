from rest_framework import serializers

from reservation.models import Reservation


class ReservationListSerializer(serializers.ModelSerializer):
    # now_queue = serializers.SerializerMethodField()
    class Meta:
        model = Reservation
        fields = (
            'id',
            'amount',
            'queue',
            'datetime',
            'is_confirm',
        )

# @staticmethod
# def now_queue(self):
#
#     queue = Reservation.objects.filter(queue=queue).last()
#     for now in queue:



