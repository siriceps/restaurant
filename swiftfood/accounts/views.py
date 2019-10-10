from django.contrib.auth import authenticate, login
from requests import Response
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import AllowAny

from .models import Account
from .serializer import LoginSerializer, RegisterSerializer, RegisterModel


class AccountLogin(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Account.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({'detail': 'you are login'}, status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        account = authenticate(username=data['username'].strip().lower(), password=data['password'])
        if account is None:
            return Response({'detail': 'username or password does not exit'}, status=status.HTTP_404_NOT_FOUND)

        login(request, account)
        return Response({}, status=status.HTTP_201_CREATED)


    # def get_queryset(self):
    #     if self.request.user.is_authenticated():
    #         return Account.objects.filter(id=self.request.user.id)
    #     else:
    #         return self.queryset


class AccountRegister(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Account.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        if Account.objects.filter(username=data['username']):
            return Response({'detail': 'username is exits'}, status=status.HTTP_409_CONFLICT)
        if Account.objects.filter(email=data['email']):
            return Response({'detail': 'email is exits'}, status=status.HTTP_409_CONFLICT)
        if data['confirm_password'] != data['password']:
            return Response({'detail': 'password is not match'}, status=status.HTTP_404_NOT_FOUND)

        data.pop('confirm_password')
        data['username'] = data['username'].lower()
        serializer = RegisterModel(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status.HTTP_201_CREATED)
