from django.db import models

class CustomManger(models.Manager):
    # def get_queryset(self): #overriding vuilt-in method called when we call all()
    #     return super().get_queryset().order_by('name')

    def get_stu_roll_range(slef,r1,r2):
        return super().get_queryset().filter(roll__range=(r1,r2))
