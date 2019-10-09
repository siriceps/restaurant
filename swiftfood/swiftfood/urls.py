from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

urlpatterns_api_user = [
    path('accounts/', include('accounts.dashboard.urls')),

]

urlpatterns_api_dashboard = [

    path('dashboard/accounts/', include('accounts.dashboard.urls')),

]

urlpatterns_swagger = [

    path('api/', get_swagger_view(title='API', patterns=urlpatterns_api_user)),
    # path('api/dashboard/', get_swagger_view(title='API Dashboard Docs.', patterns=urlpatterns_api_dashboard)),

]

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth', include('rest_framework.urls')),
]

urlpatterns += urlpatterns_api_user
urlpatterns += urlpatterns_api_dashboard
urlpatterns += urlpatterns_swagger
