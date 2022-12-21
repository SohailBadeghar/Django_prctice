from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.


class HomeTemplateView(TemplateView):
    template_name = 'myapp/home.html'


class HomeContextView(TemplateView):
    template_name = 'myapp/context.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['name']="sohail"
        context['roll_no']=12

        # context = {
        #     'name': "Sohail",
        #     'roll_no': 24
        # }
        print(context)
        print(kwargs)
        return context