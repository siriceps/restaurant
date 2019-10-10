from django.urls import path, include
from rest_framework import routers

from .views import AccountLogin, AccountRegister, LogoutView

router = routers.DefaultRouter()
router.register(r'login', AccountLogin)
router.register(r'register', AccountRegister)

urlpatterns = [

    path('logout/', LogoutView.as_view()),

]
urlpatterns += router.urls