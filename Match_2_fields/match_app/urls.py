from django.urls import path
from .views import *
urlpatterns = [
  path('POST_FORM/',showFormData,name='showFormData'),
  path('success/',thankyou,name='thankyou'),
]