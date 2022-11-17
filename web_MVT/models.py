from django.db import models
from datetime import datetime

class category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
   
class product(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    
class register(models.Model):
    firtname = models.CharField(max_length=50)
    lastname= models.CharField(max_length=50)
    phone = models.IntegerField()
    email= models.CharField(max_length=100)
    password = models.CharField(max_length=50)
 
