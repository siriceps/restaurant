from django.contrib import admin

# Register your models here.
from .models import Account, PasswordHistory


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'code',
        'username',
        'email',
        'first_name',
        'last_name',
        'is_force_reset_password',
    )

    readonly_fields = ('user_permissions',)
    actions = ['set_type_to_system_user', 'update']
    search_fields = [ 'code', 'username', 'email', 'first_name', 'last_name']

    @staticmethod
    def set_type_to_system_user(self, request, queryset):
        queryset.update(type=1)

    @staticmethod
    def update(self, request, queryset):
        for account in queryset:
            account.update_data()


@admin.register(PasswordHistory)
class PasswordHistoryAdmin(admin.ModelAdmin):
    list_display = ('account', 'password', 'datetime_create')
    search_fields = ('account__first_name', 'account__last_name', 'account__code', 'account__code2', 'account__email',
                     'account__username')

