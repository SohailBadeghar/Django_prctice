from django.db import models

# Create your models here.

class User(models.Model):
    student_name = models.CharField(max_length=100)
    techers_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    