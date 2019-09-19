from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializer import LoginSerializer
from .models import Account


class LoginView(viewsets.GenericViewSet):
    queryset = Account.objects.all()
    allow_redirects = True
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        if Config.pull_value('config-login-backend') == '1':
            data, status_response = login_azure_oauthen()
        elif Config.pull_value('config-login-backend') == '4':
            data, status_response = login_ap(request, data, True)
        elif Config.pull_value('config-login-backend') == '5':
            data, status_response = login_sansiri(request, data)
        else:
            data, status_response = login_conicle(request, data)
        return Response(data=data, status=status_response)