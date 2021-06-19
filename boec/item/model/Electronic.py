from django.db import models

from boec.item.model.Product import Product


class Electronic(Product):
    specification = models.CharField(max_length=256)
    warrantyPeriodDate = models.IntegerField(null=True)
    origin = models.CharField(max_length=256, null=True)