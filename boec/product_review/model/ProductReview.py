from django.db import models

from boec.customer.model.Account import Account
from boec.item.model.Product import Product


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True)
    comment = models.CharField(max_length=512)
    status = models.CharField(max_length=256) #APPROVED, CREATED, REMOVED
