from django.db import models


class Issues(models.Model):
    email = models.CharField(max_length=30)
    firs_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20)