from django.db import models

from boec.models.itemmodel.Product import Product


class Book(Product):
    author = models.CharField(max_length=256, null=True)
    status = models.CharField(max_length=256)
    type = models.CharField(max_length=256)