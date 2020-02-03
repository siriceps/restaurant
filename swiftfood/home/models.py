from django.db import models


class Home(models.Model):
    class Meta:
        ordering = ['sort']

    def __str__(self):
        return self.code

    @staticmethod
    def pull(id):
        try:
            return Home.objects.get(id=id)
        except Home.DoesNotExist:
            return None
