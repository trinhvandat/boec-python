from django.db import models


class EmpFullName(models.Model):
    firstName = models.CharField(max_length=256)
    midName = models.CharField(max_length=256)
    lastName = models.CharField(max_length=256)