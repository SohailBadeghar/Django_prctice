from django.db import models

# Create your models here.
class Employee(models.Model):
    Name = models.CharField(max_length=70)
    email = models.EmailField(max_length=50)
    Mobile_no = models.IntegerField()
    Department = models.CharField(max_length=50)
