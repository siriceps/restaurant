from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StockView

router = DefaultRouter()
router.register(r'stock', StockView)

urlpatterns = [

    # path(r'menu_list/', include(router.urls)),
    path('', include(router.urls)),

]
