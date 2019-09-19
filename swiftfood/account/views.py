from rest_framework import viewsets

from swiftfood.account.models import Account
from swiftfood.account.serializer import AccountSerializer


class AccountView(viewsets.GenericViewSet):
    queryset = Account.objects.none()
    serializer_class = AccountSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated():
            return Account.objects.filter(id=self.request.user.id)
        else:
            return self.queryset
