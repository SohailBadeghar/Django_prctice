# from __future__ import division
from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    Roll_no = models.IntegerField(default=False)
    Name = models.CharField(max_length=255, blank=True)
    Email = models.EmailField(max_length=255, blank=True)
    division = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True) 
    