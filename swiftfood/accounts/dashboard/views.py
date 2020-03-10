from django.utils import timezone
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from accounts.serializer import AccountRegisterSerializer
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
    queryset = Account.objects.none()
    permission_classes = (IsAuthenticated,)
    serializer_class = AccountRegisterSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Account.objects.filter(id=self.request.user.id)
        else:
            return self.queryset
