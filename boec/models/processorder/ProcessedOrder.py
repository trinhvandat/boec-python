from django.db import models

from boec.models.employeemodel.Employee import Employee
from boec.models.ordermodel.Order import Order


class ProcessedOrder(models.Model):
    processDate = models.DateField(null=True)
    status = models.CharField(max_length=256)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)