from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    
    # path('',TemplateView.as_view(template_name='myapp/home.html'),name='home')

    path('',HomeTemplateView.as_view(),name="HomeTemplateView"),

    path('home/',HomeContextView.as_view(),name="HomeContextView"),

    path('about/<int:class>/',HomeContextView.as_view(),name="cl"),



]
