from django.urls import path, include
from rest_framework import routers

from .views import AccountView, AccountManagementView

router = routers.DefaultRouter()

router.register(r'', AccountView)
router.register(r'AccountManagementView', AccountManagementView)

urlpatterns = [

    path('', include(router.urls))

]
