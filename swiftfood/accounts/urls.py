from django.urls import path
from rest_framework import routers
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from django.conf import settings

from accounts.view_change_password import ChangePasswordViewSet
from accounts.view_forget_password import ForgetPasswordView
from .views import AccountLogin, AccountRegister, LogoutView, AccountManagement

router = routers.DefaultRouter()
router.register(r'login', AccountLogin)
router.register(r'register', AccountRegister)
router.register(r'changepassword', ChangePasswordViewSet)
router.register(r'forgetpassword', ForgetPasswordView)
router.register(r'accountmanagement', AccountManagement)

urlpatterns = [

    path('logout/', LogoutView.as_view()),

]

urlpatterns += router.urls
