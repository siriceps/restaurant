from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework_swagger.views import get_swagger_view
from django.views.decorators.csrf import csrf_exempt

from accounts.view_forget_password import ConfirmPassword
from reservation.views import ReservationView

urlpatterns_api_user = [
    path('api/accounts/', include('accounts.urls')),
    path('api/menu/', include('menu.urls')),
    path('api/review/', include('review.urls')),
    path('api/mycart/', include('mycart.urls')),
    path('api/promotions/', include('promotions.urls')),
    path('api/reservation/', include('reservation.urls')),
    path('api/stock/', include('stock.urls')),

]

urlpatterns_api_dashboard = [

    path('api/dashboard/accounts/', include('accounts.dashboard.urls')),
    path('api/dashboard/menu/', include('menu.dashboard.urls')),
    path('api/dashboard/review/', include('review.dashboard.urls')),
    path('api/dashboard/promotions/', include('promotions.dashboard.urls')),
    path('api/dashboard/reservation/', include('reservation.dashboard.urls')),
    path('api/dashboard/stock/', include('stock.dashboard.urls')),

]

urlpatterns_swagger = [

    path('api/', get_swagger_view(title='API', patterns=urlpatterns_api_user)),
    path('api/dashboard/', get_swagger_view(title='API Dashboard Docs.', patterns=urlpatterns_api_dashboard)),

]

urlpatterns = [
    # url(r'^reservation/$', csrf_exempt(ReservationView)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    url(r'^api-auth', include('rest_framework.urls')),
    url(r'setpassword/$', ConfirmPassword.as_view()),
    url(r'forgetpassword/$', ConfirmPassword.as_view()),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

]

urlpatterns += urlpatterns_api_user
urlpatterns += urlpatterns_api_dashboard
urlpatterns += urlpatterns_swagger
