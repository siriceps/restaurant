from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.sessions.models import Session
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .generator import generate_code
from .models import Account
from .serializer import LoginSerializer, RegisterSerializer, AccountRegisterSerializer, RegisterStaffSerializer


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
        # elif account.password != data['password']:
        #     return Response({'detail': 'password is incorrect'}, status=status.HTTP_404_NOT_FOUND)
        print(account)
        csrf_token = login(request, account)
        return Response(csrf_token, status=status.HTTP_201_CREATED)


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
        if data['password'] != data['confirm_password']:
            return Response({'detail': 'password is not match'}, status=status.HTTP_404_NOT_FOUND)

        data.pop('confirm_password')
        data['password'] = make_password(data['password'])
        data['username'] = data['username'].lower()
        serializer = AccountRegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status.HTTP_201_CREATED, headers=headers)


class LogoutView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            account_id = request.user.id
            session_key = request.session.session_key

            logout(request)
            Session.remove(account_id, session_key)
        finally:
            return Response(status=status.HTTP_200_OK)

    def get(self, request):
        try:
            account_id = request.user.id
            session_key = request.session.session_key
            logout(request)
            Session.remove(account_id, session_key)
        finally:
            return Response(status=status.HTTP_200_OK)


class RegisterStaff(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Account.objects.filter(is_staff=True)
    permission_classes = (AllowAny,)
    serializer_class = RegisterStaffSerializer

    action_serializers = {
        'create': RegisterStaffSerializer,
        'list': RegisterStaffSerializer,
    }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        if Account.objects.filter(username=data['username']):
            return Response({'detail': 'username is exits'}, status=status.HTTP_409_CONFLICT)
        if Account.objects.filter(email=data['email']):
            return Response({'detail': 'email is exits'}, status=status.HTTP_409_CONFLICT)
        if data['password'] != data['confirm_password']:
            return Response({'detail': 'password is not match'}, status=status.HTTP_404_NOT_FOUND)

        data.pop('confirm_password')
        data['password'] = make_password(data['password'])
        data['username'] = data['username'].lower()
        serializer = AccountRegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        code = generate_code(4)
        serializer.save(is_staff=True, is_admin=True, code=code)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status.HTTP_201_CREATED, headers=headers)

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]
        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
