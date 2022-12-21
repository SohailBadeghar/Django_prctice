from django.urls import path
from .views import *
urlpatterns = [
    path('create/',StudentCreateView.as_view(),name='StudentCreateView'),
    path('studetail/<int:pk>',StudentDetailView.as_view(),name='detail'),
    path('thankyou/',ThanksTemplateView.as_view(),name='thankyou'),


]
