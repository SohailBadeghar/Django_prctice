from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

# class Hometemplateview(TemplateView):
#     template_name = 'myapp/home.html'


class Hometemplateview(TemplateView):
    template_name = 'myapp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'sohail'
        context['roll'] = '101'
        # context = {'name':'sohail','roll':'171'}
        print(context)
        print(kwargs)

        return context