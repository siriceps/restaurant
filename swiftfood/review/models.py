from django.db import models
from django.conf import settings


class Review(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    starCount = models.SmallIntegerField(default=0)
    review_text = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now_add=True)

    # @staticmethod
    # def is_user_exists(user):
    #     return Review.objects.filter(user=user).exists()
