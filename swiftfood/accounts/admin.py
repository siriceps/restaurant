from django.contrib import admin

# Register your models here.
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from rest_framework.permissions import AllowAny

from .models import Account, ForgetPassword


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'code',
        'phone',
        'image',

    )
    permission_classes = (AllowAny,)
    search_fields = ['username', 'email', 'first_name', 'last_name''phone']

    @staticmethod
    def set_type_to_system_user(self, request, queryset):
        queryset.update(type=1)

    @staticmethod
    def update(self, request, queryset):
        for account in queryset:
            account.update_data()


@admin.register(ForgetPassword)
class ForgetPassword(admin.ModelAdmin):
    list_display = ('id',)
    permission_classes = (AllowAny,)
