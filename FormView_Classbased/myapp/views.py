from django.shortcuts import render
from .forms import ContactFrom
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
# Create your views here.


class ContactFormView(FormView):
    template_name = 'myapp/contact.html'
    form_class = ContactFrom
    success_url = '/thankyou/'
    def form_valid(self,form):
        print(form)
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['msg'])
        return super().form_valid(form)
    
class ThanksTemplateView(TemplateView):
    template_name = 'myapp/thanks.html'