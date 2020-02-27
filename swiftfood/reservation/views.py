from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from reservation.models import Reservation
from reservation.serializer import ReservationDestroy, ReservationSerializer, ReservationListSerializer


class ReservationView(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.CreateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    action_serializers = {
        'create': ReservationSerializer,
        'list': ReservationListSerializer,
    }

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

        self.perform_create(serializer)
        reservation = Reservation.objects.filter(
            quantity=data['quantity'],
            user=request.user
        ).first()

        headers = self.get_success_headers(serializer.data)
        return Response(self.get_serializer(reservation).data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        count = self.get_object().all()
        # count = Reservation.objects.filter('count').delete()
        old_data = ReservationDestroy(count).data
        old_data.delete()
        # Reservation.objects.filter(count=count).all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     data = serializer.validated_data
    #     Reservation.objects.create(
    #         queue=data['queue'],
    #         quantity=data['quantity'],
    #         datetime=data['datetime'],
    #         is_confirm=data['is_confirm'],
    #     )
    #     # headers = self.get_success_headers(serializer.data)
    #     return Response(data, status=status.HTTP_201_CREATED)
