from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=100)
    installed = models.BooleanField(default=False)
    version = models.CharField(max_length=10)