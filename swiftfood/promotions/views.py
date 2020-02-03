from rest_framework import mixins, viewsets
from rest_framework.response import Response

from promotions.models import Promotions
from promotions.serializer import PromotionsListSerializer


class PromotionsView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Promotions.objects.all()
    serializer_class = PromotionsListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)