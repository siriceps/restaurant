from rest_framework import viewsets, status
from rest_framework.response import Response

from review.dashboard.serializer import ReviewSerializer
from review.models import Review


class ReviewView(viewsets.GenericViewSet):
    queryset = Review.objects.all().order_by('-date_time')
    serializer_class = ReviewSerializer

    action_serializers = {
        'create': ReviewSerializer,
        'list': ReviewSerializer,
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
        # if Review.is_user_exists(request.user):
        #     return Response(status=status.HTTP_409_CONFLICT)
        # else:
        self.perform_create(serializer)
        review = Review.objects.filter(
            review_text=data['review_text'],
            review_score=data['review_score'],
            user=request.user
        ).first()
        # headers = self.get_success_headers(serializer.data)
        return Response(self.get_serializer(review).data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

