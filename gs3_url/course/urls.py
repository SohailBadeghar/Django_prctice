from django.urls import path,include
from .views import *

urlpatterns = [
    path('show/',show,name='show'),
    path('render_page',render_page,name='render_page'),
]
