from django.db import models
from django.contrib.auth.models import AbstractUser

from .manager import Usermanager
    
# Create your models here.
class Registration_Form(AbstractUser):
    username = None
    first_name = models.CharField(max_length=100,null=False,blank=False)
    last_name = models.CharField(max_length=100,null=False,blank=False)
    email = models.EmailField(unique=True,null=False,blank=False)
    mobile_no = models.CharField(max_length=12)
    is_verified = models.BooleanField(default=False,null=True,blank=True)

    
    objects = Usermanager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []