from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from .models import OrderMenu
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)