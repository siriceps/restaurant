from rest_framework import serializers

from review.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    starCount = serializers.IntegerField(min_value=1, max_value=5)
    review_text = serializers.CharField(max_length=255)

    class Meta:
        model = Review
        fields = (
            'id',
            'user',
            'starCount',
            'review_text',
            # 'date_time',
        )

    def get_user(self, review):
        return ReviewSerializer(review.user).data