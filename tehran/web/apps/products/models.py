from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    rate = models.PositiveIntegerField()
    in_stock = models.BooleanField(default=True)
