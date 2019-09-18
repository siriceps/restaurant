from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response

from ice.account.dashboard.serializer import AccountSerializer, AccountListSerializer
from ice.account.models import Account


class AccountView(viewsets.GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    app = 'account'
    model = 'account'

    action_serializers = {
        # 'create': AccountCreateSerializer,
        'list': AccountListSerializer,
        # 'retrieve': AccountDetailSerializer,
        # 'partial_update': AccountUpdateSerializer,
    }
    # def get_serializer_class(self):
    #     if hasattr(self, 'action_serializers'):
    #         if self.action in self.action_serializers:
    #             return self.action_serializers[self.action]
    #     return super().get_serializer_class()

    def get_queryset(self):
        if self.queryset.exists():
            return self.queryset
        # elif self.request.is_organization:
        #     child_list = Organization.get_child_by_account_id(self.request.user.id)
        #     return Account.objects.filter(id__in=child_list)
        # elif self.request.is_department:
        #     department_list = Department.pull_by_account(self.request.user).values_list('id', flat=True)
        #     member_list = Member.pull_member_by_multiple_department_id(department_list).values_list('account__id',
        #                                                                                             flat=True)
        #     return Account.objects.filter(id__in=member_list)
        # elif self.request.is_group:
        #     if self.request.GROUP:
        #         return Account.objects.filter(
        #             id__in=GroupAccount.objects.filter(group=self.request.GROUP).values_list('account_id', flat=True)
        #         )
        #     else:
        #         return Account.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        # is_filter, account_id_list = filter_account_id(request)
        # if is_filter:
        #     queryset = queryset.filter(id__in=account_id_list)

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

