from django.db import models

from boec.order.model.Order import Order
from boec.order.model.Shipment import Shipment


class Payment(models.Model):
    order = models.ForeignKey(Order ,on_delete=models.CASCADE)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    total = models.FloatField(null=True)
    paymentDate = models.DateField(null=True)