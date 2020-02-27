from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from reservation.models import Reservation
from reservation.serializer import ReservationListSerializer, ReservationDestroy


class ReservationView(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.CreateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = Reservation.objects.all()
    serializer_class = ReservationListSerializer

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

    def destroy(self, request, *args, **kwargs):
        count = self.get_object()
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
