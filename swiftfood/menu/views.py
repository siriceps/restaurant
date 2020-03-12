import coreapi
from django.core.cache import cache
from rest_framework import mixins, viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema

from .serializer import MenuListSerializer, CategorySerializer, MenuUpdateSerializer
from .models import Menu


class MenuList(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuListSerializer
    search_fields = ('name', 'categories', 'price', 'material')
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
        # serializer = self.get_serializer(queryset, many=True)
        # return Response(serializer.data)


class MenuManagement(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Menu.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = MenuUpdateSerializer
    pagination_class = None

    permission_classes_action = {
        'list': [IsAuthenticated],
        'profile_patch': [IsAuthenticated],
    }

    # def get_permissions(self):
    #     try:
    #         return [permission() for permission in self.permission_classes_action[self.action]]
    #     except KeyError:
    #         return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Menu.objects.filter(id=self.request.user.id)
        else:
            return self.queryset

    def get_object(self, queryset=None):
        menu = Menu.objects.filter(pk=self.request.user.id).first()
        return menu

    def list(self, request, *args, **kwargs):
        _key = 'menu_profile_%s' % request.user.id
        _cache = cache.get(_key)
        if _cache:
            return Response(_cache)

        result = self.get_serializer(request.user).data
        cache.set(_key, result)
        return Response(result)

    def profile_patch(self, request, *args, **kwargs):
        """
            Update Profile
            ---
            Parameters:
                - first_name: string
                - last_name: string
                - image: string
                - language: string
            Response Message:
                - code: 200
                  message: ok
        """
        menu = self.get_object()
        serializer = MenuUpdateSerializer(menu, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        menu.cache_delete()
        return Response(self.get_serializer(menu).data)
