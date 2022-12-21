from django.urls import path
from .views import *
urlpatterns = [

    path('',TemplateView.as_view(template_name ='myapp/index.html'),name='templateView'),

    path('home/',RedirectView.as_view(url = '/'),name='redirectView'),

    path('geeky/',RedirectView.as_view(url = 'https://www.geekyshows.com'),name='geekyView'),

    path('google/',GoogleRedirectView.as_view(),name='googleRedirectView'),

    path('index/',RedirectView.as_view(pattern_name = 'googleRedirectView'),name='patternRedirectView'), #redirect using name of url 

    path('home/<int:pk>/',geekRedirectView.as_view(), name='geek'),
    
    path('<int:pk>/',TemplateView.as_view(template_name ='myapp/index.html'),name='mindex'),

]