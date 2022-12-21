from django.urls import path
from .views import *

urlpatterns = [
 
 path('calulator/',calculator,name='calculator'),
]
