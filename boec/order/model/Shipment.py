from django.db import models

from boec.order.model.Order import Order


class Shipment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    fee = models.FloatField(null=True)
    type = models.CharField(max_length=256, null=True)
    status = models.CharField(max_length=256, null=True)
    receiveDate = models.DateField(null=True)