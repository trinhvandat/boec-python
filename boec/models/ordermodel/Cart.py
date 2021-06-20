from django.db import models

from boec.models.customermodel.Account import Account
from boec.models.itemmodel.Item import Item


class Cart(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    total = models.IntegerField(null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)