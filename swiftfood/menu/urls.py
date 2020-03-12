from django.urls import path, include
from rest_framework.routers import DefaultRouter

from menu.view_category import Category
from .views import MenuList, MenuManagement

router = DefaultRouter()
router.register(r'menu', MenuList)
router.register(r'category', Category)
router.register(r'menuview', MenuManagement)

urlpatterns = [

    # path(r'menu_list/', include(router.urls)),
    path('', include(router.urls)),

]
