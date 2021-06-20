from django.db import models


class FullName(models.Model):
    firstName = models.CharField(max_length=256)
    midName = models.CharField(max_length=256)
    lastName = models.CharField(max_length=256)