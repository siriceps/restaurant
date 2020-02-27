from rest_framework import mixins, viewsets
from rest_framework.response import Response

from mycart.models import MyCart
from mycart.serializer import MyCartSerializer, MyCartListSerializer


class ViewToTal(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.UpdateModelMixin):
    queryset = MyCart.objects.all()
    serializer_class = MyCartSerializer

    action_serializers = {
        'create': MyCartSerializer,
        'list': MyCartListSerializer,
        'retrieve': MyCartSerializer,
    }

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        total = MyCart.objects.filter('total').first()
        if total == 0:
            total += total.get_food_menu
            return total

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
