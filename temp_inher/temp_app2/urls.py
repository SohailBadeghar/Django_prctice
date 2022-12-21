from django.urls import path
from .views import *

urlpatterns = [

    path('info/',info,name='info'),

]