from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField()
    emp_name  = models.CharField(max_length=255)
    emp_dep= models.CharField(max_length=255)
    
   