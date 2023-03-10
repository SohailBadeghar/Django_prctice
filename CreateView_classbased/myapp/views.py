from django.shortcuts import render
from django.views.generic.edit import CreateView 
from django.views.generic.detail import DetailView 
from django.views.generic.base import TemplateView
from .models import *
# Create your views here.

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email' ,'password']
    # success_url = '/thankyou/'


class ThanksTemplateView(TemplateView):
    template_name = 'myapp/thanks.html'

class StudentDetailView(DetailView):
    model = Student