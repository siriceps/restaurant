from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MenuList

router = DefaultRouter()
router.register(r'menu', MenuList)

urlpatterns = [

    # path(r'menu_list/', include(router.urls)),
    path('', include(router.urls)),

]
