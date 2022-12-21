from django.urls import path
from .views import *
urlpatterns = [

    path('mails/',send_mails,name='mail'),
   
]
