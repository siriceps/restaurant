from rest_framework import serializers

from accounts.models import Account
from .models import Review
from django.contrib.auth.models import User


class SerializerModel(serializers.ModelSerializer):
    review_score = serializers.IntegerField(min_value=1, max_value=5)
    user = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ('id',
                  'user',
                  'review_score',
                  'review_text',
                  'date_time',
                  )

    def get_user(self, review):
        return SerializerUser(review.user).data


class SerializerUser(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id',
                  'username',
                  'email',
                  )


class SerializerList(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    review_score = serializers.IntegerField(min_value=1, max_value=5)
    review_text = serializers.CharField(max_length=255)

    class Meta:
        model = Review
        fields = (
            'id',
            'user',
            'review_score',
            'review_text',
            'date_time',
        )

    def get_user(self, review):
        return SerializerUser(review.user).data
