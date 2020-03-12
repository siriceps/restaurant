from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MenuList, Category

router = DefaultRouter()
router.register(r'menu', MenuList)
router.register(r'category', Category)


urlpatterns = [

    # path(r'menu_list/', include(router.urls)),
    path('', include(router.urls)),

]