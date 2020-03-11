from rest_framework import serializers

from accounts.models import Account
from reservation.models import Reservation


class ReservationListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = (
            'id',
            'quantity',
            'queue',
            'datetime',
            'is_confirm',
            'count',
            'user',
        )

    def get_user(self, reservations):
        return SerializerUser(reservations.user).data


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    queue = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = (
            'id',
            'queue',
            'quantity',
            'user',
        )

    def get_user(self, reservations):
        return SerializerUser(reservations.user).data

    def get_queue(self):
        queue = 0
        queue += 1
        return queue


class ReservationDestroy(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = (
            'count',
            'user',
        )

    def get_user(self, reservations):
        return SerializerUser(reservations.user).data


class SerializerUser(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id',
                  'username',
                  )
