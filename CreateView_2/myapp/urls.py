from django.urls import path
from .views import *
urlpatterns = [
    path('create/',StudentCreateView.as_view(),name='StudentCreateView'),
    path('thankyou/',ThanksTemplateView.as_view(),name='thankyou'),


]
