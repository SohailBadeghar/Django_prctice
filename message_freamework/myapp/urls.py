from ctypes import alignment
from django.urls import path
from .views import *
urlpatterns = [
  path('registrations/',reg , name='registrations'),
]