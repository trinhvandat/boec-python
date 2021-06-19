from django.db import models


class EmpAddress(models.Model):
    numberHouse = models.CharField(max_length=256)
    street = models.CharField(max_length=256)
    district = models.CharField(max_length=256)
    city = models.CharField(max_length=256)