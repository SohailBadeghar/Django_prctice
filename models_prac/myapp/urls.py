from django.urls import path
from .views import *

urlpatterns = [
  path('musicians/',musicians,name='musicians'),
  # path('albums_details',albums_details,name='albums_details'),
]