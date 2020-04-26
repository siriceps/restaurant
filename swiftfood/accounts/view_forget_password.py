import coreapi
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.views import APIView

from accounts.generator import generate_token
from accounts.models import Account, ForgetPassword
from accounts.serializer import ForgetPasswordSerializer
from swiftfood.settings import EMAIL_HOST_USER


class ForgetPasswordView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = Account.objects.none()
    serializer_class = ForgetPasswordSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        # token = 'qweqweqweqweqwe'
        token = generate_token(64)
        try:
            forget = ForgetPassword.objects.create(account=Account.objects.filter(email=data['email']).first(),
                                                   token=token)
            link = str(request.get_host()) + '/return_template/' + '/?token=' + token

            print(forget.account.email)
            send_mail('reset password ', link, EMAIL_HOST_USER, [forget.account.email], fail_silently=False)

        finally:
            return Response(serializer.data, status=status.HTTP_201_CREATED)


def return_template(request):
    return render(request, 'password_reset_form.html')


class ConfirmPassword(APIView):
    permission_classes = [AllowAny]
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field("password",
                          required=True),
            coreapi.Field("confirm_password",
                          required=True),
        ]
    )

    def get(self, request, *args, **kwargs):
        request.session['token'] = request.GET.get('token', None)

        return HttpResponse("return this string")

    def post(self, request, *args, **kwargs):
        user = ForgetPassword.objects.filter(token=request.session['token']).first()
        password = request.data['password']
        confirm_password = request.data['confirm_password']
        if password is None and confirm_password is None:
            return Response({'error': 'no password or confirm password'}, status=status.HTTP_400_BAD_REQUEST)
        user.account.set_password(password)
        user.account.save()
        ForgetPassword.objects.filter(token=request.session['token']).delete()
        request.session['token'] = None
        return Response({}, status=status.HTTP_201_CREATED)


# import coreapi
# from django.core.mail import send_mail
# from django.http import HttpResponse
# from rest_framework import viewsets, mixins, status
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from rest_framework.schemas import AutoSchema
# from rest_framework.views import APIView
#
# from accounts.generator import generate_token
# from accounts.models import Account, ForgetPassword
# from accounts.serializer import ForgetPasswordSerializer
#
#
# class ForgetPasswordView(mixins.CreateModelMixin, viewsets.GenericViewSet):
#     permission_classes = [AllowAny]
#     queryset = Account.objects.none()
#     serializer_class = ForgetPasswordSerializer
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         data = serializer.validated_data
#         token = generate_token(64)
#         try:
#             forget = ForgetPassword.objects.create(account=Account.objects.filter(email=data['email']).first(),
#                                                    token=token).save()
#             link = str(request.get_host()) + '/?token=' + token
#
#             # TODO Send mail to user
#             send_mail(link, 'sir_ice39@outlook.com', forget.data['email'], fail_silently=False)
#         finally:
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class ConfirmPassword(APIView):
#     permission_classes = [AllowAny]
#     schema = AutoSchema(
#         manual_fields=[
#             coreapi.Field("password",
#                           required=True),
#             coreapi.Field("confirm_password",
#                           required=True),
#         ]
#     )
#
#     def get(self, request, *args, **kwargs):
#         request.session['token'] = request.GET.get('token', None)
#
#         return HttpResponse("return this string")
#
#     def post(self, request, *args, **kwargs):
#         user = ForgetPassword.objects.filter(token=request.session['token']).first()
#         password = request.data['password']
#         confirm_password = request.data['confirm_password']
#         if password is None and confirm_password is None:
#             return Response({'error': 'no password or confirm password'}, status=status.HTTP_400_BAD_REQUEST)
#         user.account.set_password(password)
#         user.account.save()
#         ForgetPassword.objects.filter(token=request.session['token']).delete()
#         request.session['token'] = None
#         return Response({}, status=status.HTTP_201_CREATED)
