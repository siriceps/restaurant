from django.urls import path, include
from rest_framework import routers

from .views import MenuView

router = routers.DefaultRouter()

router.register(r'menu', MenuView)

urlpatterns = [

    path('', include(router.urls))

]