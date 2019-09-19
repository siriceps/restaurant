from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response

from ..dashboard.serializer import AccountSerializer, AccountCreateSerializer, AccountListSerializer
from ..models import Account


class AccountView(viewsets.GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    # app = 'account'
    # model = 'account'

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
        serializer = self.get_serializer(page, many=True).data
        response = self.get_paginated_response(serializer).data
        return Response(response)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        account = Account.objects.create_user(data['username'], data['password'])
        account.email = data.get('email', '')
        if len(account.email) == 0:
            account.is_subscribe = False

        for field in serializer.fields:
            if field in data and field not in ['supervisor', 'department', 'position']:
                setattr(account, field, data.get(field))

        if data.get('is_active', False):
            account.last_active = timezone.now()

        account.set_password(data['password'])
        account.save()

        if 'is_force_reset_password' in data and data['is_force_reset_password']:
            account.force_reset_password()

