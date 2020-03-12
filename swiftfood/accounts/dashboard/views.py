from django.utils import timezone
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.core.cache import cache

from accounts.serializer import ProfileUpdateSerializer, AccountProfileSerializer
from ..dashboard.serializer import AccountSerializer, AccountCreateSerializer, AccountListSerializer
from ..models import Account


class AccountView(viewsets.GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    action_serializers = {
        'create': AccountCreateSerializer,
        'list': AccountListSerializer,
    }

    def get_queryset(self):
        if self.queryset.exists():
            return self.queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        account = Account.objects.create_user(data['username'], data['password'])
        account.email = data.get('email', '')
        if len(account.email) == 0:
            account.is_subscribe = False

        for field in serializer.fields:
            if field in data and field:
                setattr(account, field, data.get(field))

        if data.get('is_active', False):
            account.last_active = timezone.now()

        account.set_password(data['password'])
        account.save()

        if 'is_force_reset_password' in data and data['is_force_reset_password']:
            account.force_reset_password()


class AccountManagementView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Account.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = AccountProfileSerializer
    pagination_class = None

    permission_classes_action = {
        'list': [IsAuthenticated],
        'profile_patch': [IsAuthenticated],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Account.objects.filter(id=self.request.user.id)
        else:
            return self.queryset

    def get_object(self, queryset=None):
        user = Account.objects.filter(pk=self.request.user.id).first()
        return user

    def list(self, request, *args, **kwargs):
        _key = 'account_profile_%s' % request.user.id
        _cache = cache.get(_key)
        if _cache:
            return Response(_cache)

        result = self.get_serializer(request.user).data
        cache.set(_key, result)
        return Response(result)

    def profile_patch(self, request, *args, **kwargs):
        """
            Update Profile
            ---
            Parameters:
                - first_name: string
                - last_name: string
                - image: string
            Response Message:
                - code: 200
                  message: ok
        """
        account = self.get_object()
        serializer = ProfileUpdateSerializer(account, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        account.cache_delete()
        return Response(self.get_serializer(account).data)
