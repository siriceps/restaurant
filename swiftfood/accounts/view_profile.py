from django.core.cache import cache
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from accounts.models import Account
from accounts.serializer import ProfileUpdateSerializer


class AccountManagement(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Account.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ProfileUpdateSerializer
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
            return Account.objects.filter(id=self.request.user.id)
        else:
            return self.queryset

    def get_object(self, queryset=None):
        user = Account.objects.filter(pk=self.request.user.id).first()
        return user

    def list(self, request, *args, **kwargs):
        _key = 'account_profile_%s' % request.user.id
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
        accounts = self.get_object()
        serializer = ProfileUpdateSerializer(accounts, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        accounts.cache_delete()
        return Response(self.get_serializer(accounts).data)
