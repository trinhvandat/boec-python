from django.db import models

from boec.order.model.Payment import Payment


class CreditCard(Payment):
    nameOnCard = models.CharField(max_length=256)
    cardNumber = models.CharField(max_length=256)
    code = models.CharField(max_length=256)