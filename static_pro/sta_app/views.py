from django.shortcuts import render
from .views import *
# Create your views here.

def home(request):
    return render(request, 'sta_app/home.html',{'title':'Love in the Air' ,'cname':'Django'})
