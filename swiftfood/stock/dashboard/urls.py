from django.urls import path, include
from rest_framework import routers

from .views import StockViewAdmin

router = routers.DefaultRouter()

router.register(r'stock', StockViewAdmin)

urlpatterns = [

    path('', include(router.urls))

]
