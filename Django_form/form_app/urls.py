from django.urls import path
from .views import *

urlpatterns = [

    path('form/',showFormData,name='showFormData'),

]