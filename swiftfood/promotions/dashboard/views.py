from rest_framework import viewsets, status
from rest_framework.response import Response

from promotions.serializer import PromotionsSerializer, PromotionsListSerializer
from ..models import Promotions


class PromotionsViewAdmin(viewsets.ModelViewSet):
    queryset = Promotions.objects.all()
    serializer_class = PromotionsSerializer

    action_serializers = {
        'create': PromotionsSerializer,
        'list': PromotionsListSerializer,
    }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
    #     request_form = serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        data = serializer.validated_data
        # self.perform_create(serializer)
        Promotions.objects.create(
            promotion_name=data['promotion_name'],
            promotion_code=data['promotion_code'],
            promotion_picture=data['promotion_picture'],
            description=data['description'],
            discount=data['discount'],
            food_menu=data['food_menu'],

        )
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

