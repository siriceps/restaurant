from rest_framework import mixins, viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializer import MenuListSerializer
from .models import Menu


class MenuList(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuListSerializer

    action_serializers = {
        'list': MenuListSerializer,
    }
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return self.queryset.filter(is_display=True)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # try:
        #     Menu.objects.filter('material')
        #     return Response({'detail: out of stock'},status=status.HTTP_400_BAD_REQUEST)
        # except:
        #     serializer = self.get_serializer(queryset, many=True)
        #     return Response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)