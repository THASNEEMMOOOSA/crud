from django.db import models

# Create your models here.

class Person(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mob=models.CharField(max_length=10)
    age=models.CharField(max_length=2,blank=True)
    address=models.CharField(max_length=100)
    prof=models.CharField(max_length=100)
    eid=models.CharField(max_length=100)