from django.db import models

# Create your models here.
class Auther(models.Model):
    name = models.CharField(max_length=50)
  
    def __str__(self):
        return self.name

class Book(models.Model):
    Author = models.ForeignKey(Auther, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    num_page = models.PositiveIntegerField(default=1)

    def __str__(self)   :
        return self.title