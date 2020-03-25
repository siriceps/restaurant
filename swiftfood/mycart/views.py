from django.core.cache import cache
from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import MyCart, Order
from .serializer import MyCartListSerializer, OrderCreateSerializer, OrderListSerializer


class OrderMenuView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

    lookup_field = 'id'

    action_serializers = {
        'create': OrderCreateSerializer,
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        self.perform_create(serializer)
        my_cart = MyCart.objects.filter(
            food_menu=data['food_menu'],
            quantity=data['quantity'],
            user=request.user
        ).first()

        headers = self.get_success_headers(serializer.data)
        return Response(self.get_serializer(my_cart).data, status=status.HTTP_201_CREATED, headers=headers)


class MyCartMenuView(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = MyCart.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = MyCartListSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

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
        self.perform_create(serializer)
        my_cart = MyCart.objects.create(
            food_menu=data['food_menu'],
            quantity=data['quantity'],
            user=request.user,
        )
        headers = self.get_success_headers(serializer.data)
        return Response(self.get_serializer(my_cart).data, status=status.HTTP_201_CREATED, headers=headers)
