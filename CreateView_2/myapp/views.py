from django.shortcuts import render
from django.views.generic.edit import CreateView 
from django.views.generic.base import TemplateView
from .models import *
from django import forms
# Create your views here.

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email' ,'password']
    success_url = '/thankyou/'


    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'myclass'})


class ThanksTemplateView(TemplateView):
    template_name = 'myapp/thanks.html'

