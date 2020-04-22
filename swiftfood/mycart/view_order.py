from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from .models import MyCart, Order
from .serializer_order import OrderCreateSerializer, OrderListSerializer


class OrderMenuView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

    lookup_field = 'id'

    action_serializers = {
        'create': OrderCreateSerializer,
        'list': OrderListSerializer,
    }

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]
        return super().get_serializer_class()

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
        my_cart = MyCart.objects.filter(
            is_order=False,
        )
        for i in my_cart:
            i.total = i.food_menu.price * i.quantity
            i.save()
        serializer.save(
            my_cart=my_cart,
            datetime_order=data['datetime_order'],
            service_charge=0.1,
            vat=0.07,
            total=i.total,
            user=request.user,
        )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status.HTTP_201_CREATED, headers=headers)
