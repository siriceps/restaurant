from rest_framework import viewsets, status
from rest_framework.response import Response

from stock.models import Stock
from stock.serializer import StockListSerializer


class StockView(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
