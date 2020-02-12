from django.contrib.auth.hashers import check_password
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import Account
from accounts.serializer import ChangePasswordSerializer


class ChangePasswordViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    queryset = Account.objects.none()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        if not check_password(data['old_password'], request.user.password):
            return Response({'error': 'old password incorrect'}, status=status.HTTP_400_BAD_REQUEST)
        elif data['new_password'] != data['confirm_password']:
            return Response({'error': '2 password not match'}, status=status.HTTP_400_BAD_REQUEST)

        request.user.set_password(data['new_password'])
        request.user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
