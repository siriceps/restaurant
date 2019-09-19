
from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework import routers

from swiftfood.account.dashboard.views import AccountView

router = routers.DefaultRouter()


router.register(r'', AccountView)

urlpatterns = [

    path('', include(router.urls))

]