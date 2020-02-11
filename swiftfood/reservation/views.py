from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from reservation.models import Reservation
from reservation.serializer import ReservationListSerializer


class ReservationView(mixins.ListModelMixin, viewsets.GenericViewSet):
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
    #     request_form = serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        data = serializer.validated_data
        # self.perform_create(serializer)
        Reservation.objects.create(
            queue=data['queue'],
            amount=data['amount'],
            datetime=data['datetime'],
            is_confirm=data['is_confirm'],
        )
        # headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED)