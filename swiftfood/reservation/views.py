from rest_framework import mixins, viewsets, status
from rest_framework import mixins, viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from reservation.models import Reservation
from reservation.serializer import ReservationSerializer, ReservationListSerializer


class ReservationView(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.CreateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = Reservation.objects.all().order_by('datetime')
    serializer_class = ReservationSerializer
    permission_classes = (AllowAny,)

    action_serializers = {
        'create': ReservationSerializer,
        'list': ReservationListSerializer,
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
        data = serializer.validated_data
        serializer.save(queue=Reservation.count())
        # serializer.save(queue=Reservation.count(), user=request.user)
        headers = self.get_success_headers(serializer.data)
        # return Response(self.get_serializer(reservation).data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     data = serializer.validated_data
    #     self.perform_create(serializer)
    #     reservation = Reservation.objects.filter(
    #         quantity=data['quantity'],
    #         user=request.user
    #     ).first()
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(self.get_serializer(reservation).data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        reservation = self.get_object()
        self.perform_destroy(reservation)
        reser = Reservation.objects.filter(queue__gte=reservation.queue)
        for i in reser:
            i.queue -= 1
            i.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
