from django.db import models


class Stock(models.Model):
    material_name = models.CharField(max_length=50, db_index=True, blank=True)
    amount_material = models.SmallIntegerField(default=0)
    material_picture = models.ImageField(upload_to='stock/%Y/%m/', null=True, blank=True)
