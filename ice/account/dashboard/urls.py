from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from ice.account.dashboard.views import AccountView

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),

]
router.register(r'', AccountView)