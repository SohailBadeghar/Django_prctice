from django.shortcuts import render
from django.views.generic.base import TemplateView ,RedirectView
# Create your views here.

class GoogleRedirectView(RedirectView):
    url = 'https://docs.djangoproject.com/'


class geekRedirectView(RedirectView):
    pattern_name ='mindex'