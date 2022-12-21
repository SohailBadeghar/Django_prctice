from django.db import models

from myapp.mangers import CustomManger

# Create your models here.
class Student(models.Model):    
    name = models.CharField(max_length=200) 
    roll = models.IntegerField()

    students = CustomManger()   #custome manager written
    # objects = models.Manager()    # Default Django provide this model manger

