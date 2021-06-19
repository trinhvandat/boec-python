from django.db import models

from boec.employee.model.EmpAccount import EmpAccount
from boec.employee.model.EmpAddress import EmpAddress
from boec.employee.model.EmpFullName import EmpFullName


class Employee(models.Model):
    email = models.CharField(max_length=256)
    code = models.CharField(max_length=256)
    salary = models.FloatField(max_length=256)
    position = models.CharField(max_length=256)
    dob = models.DateField(null=True)
    name = models.ForeignKey(EmpFullName, on_delete=models.CASCADE)
    account = models.ForeignKey(EmpAccount, on_delete=models.CASCADE)
    address = models.ForeignKey(EmpAddress, on_delete=models.CASCADE)