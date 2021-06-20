from django.db import models

from boec.models.employeemodel.Employee import Employee
from boec.models.productreviewmodel.ProductReview import ProductReview


class ProductReviewProcessed(models.Model):
    processedDate = models.DateField(null=True)
    status = models.CharField(max_length=256) #APPROVED, REMOVED
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    productReview = models.ForeignKey(ProductReview, on_delete=models.CASCADE)