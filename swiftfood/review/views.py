from django.db.models import Avg
from django.db.models import Count
from rest_framework.response import Response
from .models import Review
from .serializer import SerializerModel, SerializerList
from rest_framework import viewsets
from rest_framework import status
from rest_framework import mixins


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-date_time')
    serializer_class = SerializerList

    action_serializers = {
        'create': SerializerModel,
        'list': SerializerList,
    }

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]
        return super().get_serializer_class()

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

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class Average(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = SerializerList

    def list(self, request, *args, **kwargs):
        average = Review.objects.aggregate(Avg('review_score'))

        return Response({'average': average})


class SumOfEachScore(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = SerializerList

    def list(self, request, *args, **kwargs):
        sum_of_each = Review.objects.values('review_score').annotate(count=Count('review_score'))
        return Response({'sum of each': sum_of_each})


class CountReview(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = SerializerList

    def list(self, request, *args, **kwargs):
        # count_review = Review.objects.values('review_text')
        queryset = self.filter_queryset(self.get_queryset())
        return Response({'count_review': queryset.count()})
