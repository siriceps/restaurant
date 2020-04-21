from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import MyCart
from .serializer import MyCartListSerializer


class MyCartMenuView(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = MyCart.objects.all()
    permission_classes = (AllowAny,)
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
