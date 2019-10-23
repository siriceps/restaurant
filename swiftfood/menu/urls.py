from django.urls import path, include
from rest_framework import routers

from .views import MenuList

router = routers.DefaultRouter()
router.register(r'list of menu', MenuList)

urlpatterns = [

    path('', include(router.urls))

]
urlpatterns += router.urls