from django.conf import settings
from rest_framework.permissions import BasePermission
from rest_framework import permissions


def _check_super(request):
    return request.user.is_authenticated and \
           (request.user.groups.filter(id=settings.SUPER_ADMIN_GROUP_ID) or request.user.is_superuser)


class IsSuperAdmin(BasePermission):

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True

        return _check_super(request)


class IsOwnAccount(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id


class IsSuperAdminOrIsOwnerAccount(BasePermission):

    def has_permission(self, request, view):
        return _check_super(request)

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id


class IsAccess(BasePermission):
    message = 'No one access.'

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return True


class IsNoAccess(BasePermission):
    message = 'No one access.'

    def has_permission(self, request, view):
        return False

    def has_object_permission(self, request, view, obj):
        return False
