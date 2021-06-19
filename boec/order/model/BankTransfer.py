from django.db import models

from boec.order.model.Payment import Payment


class BankTransfer(Payment):
    bankName = models.CharField(max_length=256)
    accountNumber = models.CharField(max_length=256)