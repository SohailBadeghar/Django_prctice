from django.urls import path
from .views import *
urlpatterns = [
    path('set/',setcookies,name="setcookies"),
    path('get/',getcookies,name="getcookies"),
    path('del/',delcookies,name="delcookies"),


]
