from django.contrib import admin

from reservation.models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'queue',
            'amount',
            'datetime',
            'is_confirm',
    )
