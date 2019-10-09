from django.urls import path, include
from rest_framework import routers

from .views import AccountLogin, AccountRegister

router = routers.DefaultRouter()
router.register(r'login', AccountLogin)
router.register(r'register', AccountRegister)

urlpatterns = [

    path('', include(router.urls)),

]
urlpatterns += router.urls