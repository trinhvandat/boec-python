from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256)
    priceEntry = models.IntegerField()
    dateEntry = models.DateField(null=True)
    publicationDate = models.DateField(null=True)
    barcode = models.CharField(max_length=256, null=True)
    producer = models.CharField(max_length=256, null=True)