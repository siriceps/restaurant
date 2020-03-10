from rest_framework import viewsets, status
from rest_framework.response import Response

from reservation.serializer import ReservationListSerializer
from ..models import Reservation


class ReservationViewAdmin(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationListSerializer

    action_serializers = {
        'create': ReservationListSerializer,
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
