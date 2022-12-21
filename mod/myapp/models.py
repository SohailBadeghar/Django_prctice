from django.db import models

# Create your models here.
class StudentModel(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=255)
    student_email = models.EmailField(max_length=255)
    student_password = models.CharField(max_length=255)