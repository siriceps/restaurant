from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .view_order import OrderMenuView
from .view_total import OrderTestView, MyCartTestView
from .views import MyCartMenuView

router = DefaultRouter()
router.register(r'order', OrderMenuView)
router.register(r'mycart', MyCartMenuView)
router.register(r'ordertest', OrderTestView)
router.register(r'mycarttest', MyCartTestView)

urlpatterns = [

    # path(r'menu_list/', include(router.urls)),
    path('', include(router.urls)),

]
