from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from .models import *
# Create your views here.


class StudentListView(ListView):
    model = Student
    # template_name = "myapp/student.html" '''if you want to set your templaye name then you can use this template_name in list view'''
    # context_object_name = 'student'

    '''
    This is for passing the context name and 
    this query will return the output to the template.
    '''
    # def get_queryset(self):
    #     return Student.objects.filter(course = 'python') 
    

    # '''
    # This is using get_context_data for getting data by key.
    # '''

    # def get_context_data(self, *args, **kwargs ):
    #     context = super().get_context_data(*args,**kwargs)
    #     context['freshers'] = Student.objects.all().order_by('id')
    #     return context
    




class StudentDetailView(DetailView):
    model = Student