from django.urls import path
from .views import ShowFromData

urlpatterns = [
   path('show/',ShowFromData,name="Show from"),
]