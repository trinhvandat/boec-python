from django.db import models

from boec.customer.model.Account import Account
from boec.item.model.Item import Item


class Cart(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    total = models.IntegerField(null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)