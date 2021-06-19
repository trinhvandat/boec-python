from django.db import models

from boec.employee.model.Employee import Employee
from boec.product_review.model.ProductReview import ProductReview


class ProductReviewProcessed(models.Model):
    processedDate = models.DateField(null=True)
    status = models.CharField(max_length=256) #APPROVED, REMOVED
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    productReview = models.ForeignKey(ProductReview, on_delete=models.CASCADE)