from django.db import models

from boec.models.customermodel.Account import Account
from boec.models.customermodel.Address import Address
from boec.models.customermodel.FullName import FullName


class Customer(models.Model):
    email = models.CharField(max_length=256)
    phoneNumber = models.CharField(max_length=11)
    fullName = models.ForeignKey(FullName, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __getName__(self):
        return self.fullName.firstName + " " + self.fullName.midName + " " + self.fullName.lastName