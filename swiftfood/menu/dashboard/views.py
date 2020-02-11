from rest_framework import viewsets, status
from rest_framework.response import Response

from menu.serializer import MenuListSerializer
from ..dashboard.serializer import MenuSerializer
from ..models import Menu


class MenuView(viewsets.ModelViewSet):
    queryset = Menu.objects.all().order_by('categories')
    serializer_class = MenuSerializer

    action_serializers = {
        'create': MenuSerializer,
        'list': MenuListSerializer,
    }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
    #     request_form = serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        data = serializer.validated_data
        # self.perform_create(serializer)
        Menu.objects.create(
            categories=data['categories'],
            menu_name=data['menu_name'],
            price=data['price'],
            # menu_image=data['menu_image'],
            discount_price=data['discount_price'],
            description=data['description'],
            date_exp=data['date_exp'],
            material=data['material'],
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