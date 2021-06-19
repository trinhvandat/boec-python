from django.db import models

from boec.item.model.Product import Product


class Clothes(Product):
    band = models.CharField(max_length=256, null=True)
    size = models.CharField(max_length=256)