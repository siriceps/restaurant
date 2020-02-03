from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

from menu.views import MenuList

urlpatterns_api_user = [
    path('api/accounts/', include('accounts.urls')),
    path('api/menu/', include('menu.urls')),
    path('api/review/', include('review.urls')),
    path('api/order/', include('order.urls')),
    path('api/promotions/', include('promotions.urls')),

]

urlpatterns_api_dashboard = [

    path('api/dashboard/accounts/', include('accounts.dashboard.urls')),
    path('api/dashboard/menu/', include('menu.dashboard.urls')),
    path('api/dashboard/review/', include('review.dashboard.urls')),
    path('api/dashboard/promotions/', include('promotions.dashboard.urls')),

]

urlpatterns_swagger = [

    path('api/', get_swagger_view(title='API', patterns=urlpatterns_api_user)),
    path('api/dashboard/', get_swagger_view(title='API Dashboard Docs.', patterns=urlpatterns_api_dashboard)),

]

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth', include('rest_framework.urls')),
]

urlpatterns += urlpatterns_api_user
urlpatterns += urlpatterns_api_dashboard
urlpatterns += urlpatterns_swagger
