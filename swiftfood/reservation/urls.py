from django.urls import path, include
from rest_framework.routers import DefaultRouter

from reservation.views import ReservationView

router = DefaultRouter()
router.register(r'reservation', ReservationView)

urlpatterns = [
    # url(r'^reservation/$', csrf_exempt(ReservationView)),
    path('', include(router.urls)),

]
