from django.db import models

from boec.models.itemmodel.Product import Product


class Clothes(Product):
    band = models.CharField(max_length=256, null=True)
    size = models.CharField(max_length=256)