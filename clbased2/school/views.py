from django.shortcuts import render,HttpResponse
from django.views import View
from .froms import *
# Create your views here.

def homefun(request):
    return render(request, 'school/home.html')


#Class Based View
class HomeClassView(View):
    def get(self, request):
        return render(request, 'school/home.html')


#######################################################################

def AboutFun(request):
    context = {'msg':'Welcome to Function Based View '}
    return render(request, 'school/About.html',context)


#Class Based View

class AboutClassView(View):
    def get(self, request):
        context = {'msg':'Welcome to Class Based View '}
        return render(request, 'school/About.html',context)

#############################################################################################

# function Based View
def contactfun(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse("<h1>Thank you For Registration</h1>")
    
    else:
        form = ContactForm()
        return render(request, 'school/contact.html', {'fm': form})


# class Based Views

class ContactClassView(View):

    def get(self, request):
        form = ContactForm()
        return render(request, 'school/contact.html', {'fm': form})

    def post(self, request):    
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse("<h1>Thank you For Registration</h1>")


################################################################################################ 

