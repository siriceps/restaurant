from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from .models import Stock
from .serializer import StockSerializer


class StockView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

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
    #     request_form = serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        data = serializer.validated_data
        # self.perform_create(serializer)

        Stock.objects.create(
            material_name=data['material_name'],
            amount_material=data['amount_material'],
            material_picture=data['material_picture'],
        )
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
