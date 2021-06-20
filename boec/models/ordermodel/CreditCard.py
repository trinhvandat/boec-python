from django.db import models

from boec.models.ordermodel.Payment import Payment


class CreditCard(Payment):
    nameOnCard = models.CharField(max_length=256)
    cardNumber = models.CharField(max_length=256)
    code = models.CharField(max_length=256)