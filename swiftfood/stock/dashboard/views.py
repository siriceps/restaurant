from rest_framework import viewsets, status, mixins
from rest_framework.response import Response

from stock.dashboard.serializer import StockSerializer
from stock.models import Stock


class StockViewAdmin(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    action_serializers = {
        'create': StockSerializer,
        'list': StockSerializer,
    }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

#
# class CountMaterial(mixins.ListModelMixin, viewsets.GenericViewSet):
#     queryset = Stock.objects.all()
#     serializer_class = StockSerializer
#
#     def list(self, request, *args, **kwargs):
#         count_material = Stock.objects.values('material_name', 'quantity_material')
#         if count_material.quantity_material <= 2:
#             return Response({'detail almost out of stock'})
#         elif count_material.quantity_material == 0:
#             return Response({'detail out of stock'})