from django.urls import path
from .views import *

urlpatterns = [
    # path('show/<my_id>/',show,name='show'),
    path('show/<int:my_id>/',show,name='show'),

    path('',dynamic,name='dynamic'),

]