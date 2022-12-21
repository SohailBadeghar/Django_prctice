from django.urls import path
from .views import *
urlpatterns = [
    # path('dyanamic_temp',Dyanamic_template,name='dyanamic_temp'),
    path('datetime',datetime,name='datetime'),
]