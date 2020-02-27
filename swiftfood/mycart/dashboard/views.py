from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from accounts.models import Account
from menu.models import Menu
from mycart.models import MyCart
from .serializer import OrderListSerializer


class OrderMenuView(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = MyCart.objects.all()
    serializer_class = OrderListSerializer

    action_serializers = {
        'create': OrderListSerializer,
        'list': OrderListSerializer,
    }

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     data = serializer.validated_data
    #
    #
    #     if 'account_username' in data:
    #         account = Account.objects.filter(username=data['account_username']).first()
    #     if account is None:
    #         return Response({'detail': 'Account not found'}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     mycart = OrderMenu.objects.create(
    #         food_menu=data['food_menu'],
    #         quantity=data['quantity'],
    #         datetime=data['datetime'],
    #         service_charge=data['service_charge'],
    #         vat=data['vat'],
    #         total=data['total'],
    #         user=request.user
    #     ).first()
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(self.get_serializer(mycart).data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        total = self.get_object()
        total = total.get_food_menu
        serializer = self.get_serializer(total)
        return Response(serializer.data)
