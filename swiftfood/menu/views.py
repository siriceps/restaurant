from rest_framework import mixins

from .serializer import MenuListSerializer
from .models import Menu


class MenuList(mixins.ListModelMixin):
    queryset = Menu.objects.all()
    serializer_class = MenuListSerializer


