from rest_framework import viewsets, status
from rest_framework.response import Response

from promotions.generator_code import gen_code
from promotions.models import Promotions
from promotions.serializer import PromotionsListSerializer


class PromotionsView(viewsets.ModelViewSet):
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        code = gen_code(64)
        # serializer.save(code=code)
        # Promotions.objects.create(
        #     promotion_name=data['promotion_name'],
        #     promotion_code=code,
        #     # promotion_picture data['promotion_picture'],
        #     description=data['description'],
        #     discount=data['discount'],
        #     promotion_menu=data['promotion_menu'],
        #     # datetime_exp=data['datetime_exp']
        # )
        # serializer = PromotionsListSerializer

        serializer.save(
            promotion_code=code,
        )

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
