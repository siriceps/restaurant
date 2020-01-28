from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import OrderMenuView

router = DefaultRouter()
router.register(r'order', OrderMenuView)

urlpatterns = [

    # path(r'menu_list/', include(router.urls)),
    path('', include(router.urls)),

]
