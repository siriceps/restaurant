
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('views/', include('account.urls')),
    path('api/dashboard/account/', include('account.dashboard.urls')),

]
