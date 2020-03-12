from django.urls import path
from rest_framework import routers

from accounts.view_change_password import ChangePasswordViewSet
from accounts.view_forget_password import ForgetPasswordView
from accounts.view_profile import AccountManagement
from .views import AccountLogin, AccountRegister, LogoutView

router = routers.DefaultRouter()
router.register(r'login', AccountLogin)
router.register(r'register', AccountRegister)
router.register(r'changepassword', ChangePasswordViewSet)
router.register(r'forgetpassword', ForgetPasswordView)
router.register(r'accounviewprofile', AccountManagement)

urlpatterns = [

    path('logout/', LogoutView.as_view()),

]

urlpatterns += router.urls
