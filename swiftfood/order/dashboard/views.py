from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from menu.models import Menu
from order.models import OrderMenu
from .serializer import OrderListSerializer


class OrderMenuView(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = OrderMenu.objects.all()
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
    #
    #     data = serializer.validated_data
    #
    #     order = OrderMenu.objects.create(
    #         food_menu=data['food_menu'],
    #         amount=data['amount'],
    #         datetime=data['datetime'],
    #         service_charge=data['service_charge'],
    #         vat=data['vat'],
    #         total=data['total'],
    #         user=request.user
    #     ).first()
    #     price = order.object.food_menu.pice
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(self.get_serializer(order).data, status=status.HTTP_201_CREATED, headers=headers)