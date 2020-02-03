from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PromotionsView

router = DefaultRouter()
router.register(r'promotions', PromotionsView)

urlpatterns = [

    # path(r'menu_list/', include(router.urls)),
    path('', include(router.urls)),

]
