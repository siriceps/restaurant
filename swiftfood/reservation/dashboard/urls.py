from django.urls import path, include
from rest_framework import routers

from .views import ReservationViewAdmin

router = routers.DefaultRouter()

router.register(r'reservation', ReservationViewAdmin)

urlpatterns = [

    path('', include(router.urls))

]
