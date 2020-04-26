from rest_framework import mixins, viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import MyCart, Order
from .serializer import MyCartListSerializer, MyCartSerializer
from .serializer_order import OrderCreateSerializer, OrderListSerializer


class MyCartMenuView(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = MyCart.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = MyCartSerializer
    action_serializers = {
        'create': MyCartSerializer,
        'list': MyCartListSerializer,
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
        # MyCart.objects.filter('food_menu')
        serializer.save()
        # my_cart = MyCart.objects.create(
        #     food_menu=data['food_menu'],
        #     quantity=data['quantity'],
        #     user=request.user,
        # )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status.HTTP_201_CREATED, headers=headers)
