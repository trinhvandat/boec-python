from django.db import models

from boec.item.model.Product import Product


class Item(models.Model):
    name = models.CharField(max_length=256)
    discount = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    title = models.CharField(max_length=256, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)