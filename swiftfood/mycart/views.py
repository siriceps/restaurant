from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from .models import MyCart
from .serializer import MyCartListSerializer, OrderSerializer


class OrderMenuView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    queryset = MyCart.objects.all()
    serializer_class = MyCartListSerializer

    action_serializers = {
        'create': MyCartListSerializer,
        'list': MyCartListSerializer,
        'retrieve': OrderSerializer,
    }

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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     food_total = MyCart.objects.filter('total').first()
    #
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     data = serializer.validated_data
    #     if Review.is_user_exists(request.user):
    #         return Response(status=status.HTTP_409_CONFLICT)
    #     else:
    #         self.perform_create(serializer)
    #     review = Review.objects.filter(
    #         review_text=data['review_text'],
    #         review_score=data['review_score'],
    #         user=request.user
    #     ).first()
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(self.get_serializer(review).data, status=status.HTTP_201_CREATED, headers=headers)
