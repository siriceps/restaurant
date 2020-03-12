import coreapi
from rest_framework import viewsets, mixins
from rest_framework.schemas import AutoSchema

from menu.models import Menu
from menu.serializer import CategorySerializer


class Category(viewsets.GenericViewSet):
    queryset = Menu.objects.all()
    serializer_class = CategorySerializer

    schema = AutoSchema(
        manual_fields=[
            coreapi.Field("type",
                          required=True),
        ]
    )

    def list(self, request, *args, **kwargs):
        type = request.GET.get('type', None)
        queryset = self.get_queryset().filter(categories=type)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)