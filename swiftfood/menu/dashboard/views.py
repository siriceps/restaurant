from rest_framework import viewsets, status
from rest_framework.response import Response

from ..dashboard.serializer import MenuSerializer
from ..models import Menu


class MenuView(viewsets.ModelViewSet):
    queryset = Menu.objects.all().order_by('categories')
    serializer_class = MenuSerializer

    action_serializers = {
        'create': MenuSerializer,
        'list': MenuSerializer,
    }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        self.perform_create(serializer)
        Menu.objects.create(
            categories=data['categories'],
            menu_name=data['menu_name'],
            price=data['price'],
            menu_image=data['menu_image']
        )
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

