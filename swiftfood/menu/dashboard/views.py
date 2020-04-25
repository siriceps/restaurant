from django.core.cache import cache
from rest_framework import viewsets, status, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from menu.dashboard.serializer import MenuCreateSerializerAdmin, MenuSerializer
from menu.serializer import MenuUpdateSerializer, MenuListSerializer
from ..models import Menu


class MenuManagementAdmin(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Menu.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = MenuUpdateSerializer
    pagination_class = None

    action_serializers = {
        'list': MenuUpdateSerializer,
        'create': MenuCreateSerializerAdmin,
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
        menu = self.get_object()
        serializer = MenuUpdateSerializer(menu, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        menu.cache_delete()
        return Response(self.get_serializer(menu).data)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class MenuView(viewsets.ModelViewSet):
    queryset = Menu.objects.all().order_by('categories')
    serializer_class = MenuSerializer

    action_serializers = {
        'create': MenuSerializer,
        'list': MenuListSerializer,
    }

    #
    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]
        return super().get_serializer_class()

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     data = serializer.validated_data
    #     account = Account.objects.filter('id').first()
    #     if account == data['user']:
    #         if account.is_admin is True or account.is_staff is True:
    #             self.perform_create(serializer)
    #             headers = self.get_success_headers(serializer.data)
    #             return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #         else:
    #             return Response({'error': 'detail you have not permission '}, status=status.HTTP_401_UNAUTHORIZED)
    #     else:
    #         return Response({'error': 'detail you have not permission '}, status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#
# def list(self, request, *args, **kwargs):
#     queryset = self.filter_queryset(self.get_queryset())
#     page = self.paginate_queryset(queryset)
#     if page is not None:
#         serializer = self.get_serializer(page, many=True)
#         return self.get_paginated_response(serializer.data)
#
#     serializer = self.get_serializer(queryset, many=True)
#     return Response(serializer.data)

# def create(self, request, *args, **kwargs):
#     serializer = self.get_serializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     #     request_form = serializer.save()
#     #     return Response(serializer.data, status=status.HTTP_201_CREATED)
#     data = serializer.validated_data
#     import pdb
#     pdb.set_trace()
#     # self.perform_create(serializer)
#     obj_material = []
#     for obj in data['material']:
#         obj_material.append(Stock.objects.filter(id=obj))
#     # material = set(Menu.objects.filter(
#     #     material=obj_material
#     # ))
#     Menu.objects.create(
#         categories=data['categories'],
#         menu_name=data['menu_name'],
#         price=data['price'],
#         # menu_image=data['menu_image'],
#         discount_price=data['discount_price'],
#         description=data['description'],
#         # date_exp=data['date_exp'],
#     )
#
#     headers = self.get_success_headers(serializer.data)
#     return Response(data, status=status.HTTP_201_CREATED, headers=headers)
