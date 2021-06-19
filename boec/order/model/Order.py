from django.db import models

from boec.customer.model.Customer import Customer
from boec.item.model.Item import Item


class Order(models.Model):
    createDate = models.DateField(null=True)
    total = models.FloatField(null=True)
    code = models.CharField(max_length=256, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    status = models.CharField(max_length=256)  #CREATED, APPROVED, CANCELED