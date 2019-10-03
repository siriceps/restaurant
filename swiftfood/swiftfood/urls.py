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

    path('api/', get_swagger_view(title='API Docs.', patterns=urlpatterns_api_user)),
    path('api/dashboard/', get_swagger_view(title='API Dashboard Docs.', patterns=urlpatterns_api_dashboard)),

]

urlpatterns = [
    path('admin/', admin.site.urls),
    # # path('views/', include('accounts.urls')),
    # path('api/', get_swagger_view(title='API Docs.', patterns=urlpatterns_api_user)),

    # path('api/dashboard/account/', include('account.dashboard.urls')),

]

urlpatterns += urlpatterns_api_user
urlpatterns += urlpatterns_swagger
urlpatterns += urlpatterns_api_dashboard