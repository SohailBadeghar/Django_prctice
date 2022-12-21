from django.urls import path
from .views import student_form,techer_form
urlpatterns = [
    
    path('stu/',student_form, name='student_form'),
    path('tech/',techer_form, name='techer_form'),
]