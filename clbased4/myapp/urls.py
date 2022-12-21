from django.urls import path
from .views import *
urlpatterns = [
    path('',TemplateView.as_view(template_name="myapp/home.html"),name="Blankhome"),

    path('home/',RedirectView.as_view(url='/'),name="home"),
    path('index/',RedirectView.as_view(url='/'),name="index"),

    path('google/',RedirectView.as_view(url='https://www.google.co.in/'),name="google"),


]