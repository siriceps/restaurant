from rest_framework import serializers

from accounts.models import Account
from .models import Review


class SerializerModel(serializers.ModelSerializer):
    starCount = serializers.IntegerField(min_value=1, max_value=5)
    # user = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ('id',
                  # 'user',
                  'starCount',
                  'review_text',
                  'date_time',
                  )

    # def get_user(self, review):
    #     return SerializerUser(review.user).data


class SerializerUser(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id',
                  'username',
                  'email',
                  )


class SerializerList(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    starCount = serializers.IntegerField(min_value=1, max_value=5)
    review_text = serializers.CharField(max_length=255)

    class Meta:
        model = Review
        fields = (
            'id',
            # 'user',
            'starCount',
            'review_text',
            'date_time',
        )

    # def get_user(self, review):
    #     return SerializerUser(review.user).data
