from django.contrib import admin

from reservation.models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'queue',
        'quantity',
        'datetime',
        'is_confirm',
        'count',
        'user',
    )
