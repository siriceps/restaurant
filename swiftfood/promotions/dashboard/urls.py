from django.urls import path, include
from rest_framework import routers

from .views import PromotionsViewAdmin

router = routers.DefaultRouter()

router.register(r'promotions', PromotionsViewAdmin)

urlpatterns = [

    path('', include(router.urls))

]
