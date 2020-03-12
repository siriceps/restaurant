from django.urls import path, include
from rest_framework import routers

# from .views import MenuView
from menu.dashboard.views import MenuManagementAdmin, MenuView

router = routers.DefaultRouter()

router.register(r'menu', MenuView)
router.register(r'menu', MenuManagementAdmin)

urlpatterns = [

    path('', include(router.urls))

]
