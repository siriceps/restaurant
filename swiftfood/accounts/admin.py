from django.contrib import admin

# Register your models here.
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from rest_framework.permissions import AllowAny

from .models import Account, PasswordHistory


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        # 'code',
        'username',
        'email',
        'first_name',
        'last_name',

    )
    permission_classes = (AllowAny,)
    readonly_fields = ('user_permissions',)
    actions = ['set_type_to_system_user', 'update']
    search_fields = ['code', 'username', 'email', 'first_name', 'last_name']

    @staticmethod
    def set_type_to_system_user(self, request, queryset):
        queryset.update(type=1)

    @staticmethod
    def update(self, request, queryset):
        for account in queryset:
            account.update_data()

#
# class UserCreationForm(forms.ModelForm):
#     """A form for creating new users. Includes all the required
#     fields, plus a repeated password."""
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#
#     class Meta:
#         model = Account
#         fields = ('email', 'date_of_birth')
#
#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2
#
#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ('username', 'email', 'password',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

#
# @admin.register(PasswordHistory)
# class PasswordHistoryAdmin(admin.ModelAdmin):
#     list_display = ('account', 'password', 'datetime_create')
#     search_fields = ('account__first_name', 'account__last_name', 'account__code', '', 'account__email',
#                      'account__username')
#
