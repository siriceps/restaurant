from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from mycart.models import OrderTest, MyCartTest
from mycart.serializer import OrderTestSerializer, MyCartTestSerializer, OrderTestCreateSerializer, \
    MyCartTestOrderSerializer


class OrderTestView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = OrderTest.objects.all()
    serializer_class = OrderTestCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order = serializer.save()
        my_cart = MyCartTest.objects.filter(is_confirm=False).first()
        if not my_cart:
            my_cart = MyCartTest.objects.create()
        order.my_cart = my_cart
        order.food_menu.material.quantity_material -= order.food_menu.material_quantity * order.quantity
        order.save()
        order.food_menu.material.save()
        my_cart.update_total_price()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class MyCartTestView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = MyCartTest.objects.all()
    serializer_class = MyCartTestSerializer

    action_serializers = {
        'order': MyCartTestOrderSerializer
    }

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]
        return super().get_serializer_class()

    def retrieve(self, request, *args, **kwargs):
        my_cart = self.get_object()
        serializer = self.get_serializer(my_cart)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False)
    def order(self, request, *args, **kwargs):
        my_cart = MyCartTest.objects.filter(is_confirm=False).first()
        if not my_cart:
            return Response([])
        serializer = self.get_serializer(my_cart)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False)  # update check bill detail false=don't need id True=require id
    def check_bill(self, request, *args, **kwargs):
        my_cart = MyCartTest.objects.filter(is_confirm=False).first()
        if not my_cart:
            return Response({'detail:No order'}, status.HTTP_404_NOT_FOUND)
        my_cart.is_confirm = True
        my_cart.save()
        serializer = self.get_serializer(my_cart)
        return Response(serializer.data)

    # def destroy(self, request, *args, **kwargs):
    #     reservation = self.get_object()
    #     self.perform_destroy(reservation)
    #     reser = Reservation.objects.filter(queue__gte=reservation.queue)
    #     for i in reser:
    #         i.queue -= 1
    #         i.save()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    # serializer = self.get_serializer(data=request.data)
    # serializer.is_valid(raise_exception=True)
    # my_cart = OrderTest.objects.filter(is_confirm=)
    # total = 0
    # for i in my_cart:
    #     i.total = i.food_menu.price * i.quantity
    #     # i.food_menu.material.quantity_material -= i.food_menu.material_quantity * i.quantity
    #     total += i.total
    #     i.save()
    # total = total * 0.7
    #
    # serializer.save(total=total)
    # headers = self.get_success_headers(serializer.data)
    # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
