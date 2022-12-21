from django.shortcuts import render,HttpResponse
from django.views import View
from .forms import ContactForms
# Create your views here.


#function Based View
def func_based(request):
    return HttpResponse("<h1> Function Based View</h1>")

#class Based views
# Based Class
class Fucn_based(View):
    name = "Sohail"
    def get(self, request):
        # return HttpResponse(" <h1> Hello, world! ,This is a class Based View! </h1>")
        return HttpResponse(self.name)

#Based Child Class

class Fucn_basedchild(Fucn_based):
    def get(self,request):
        return HttpResponse(self.name)



# To render template get method of class based view
class HomeView(View):
    def get(self,request):
        return render(request,'myapp/home.html')



# If you want to pass the Dta through context 

class AboutClassView(View):
    def get(self,request):
        context = {
            'msg':'ALL IS WELL!'
        }
        return render(request,'myapp/about.html',context)








#Using Forms function based

def contactfun(request):
    if request.method == 'POST':
        forms = ContactForms(request.POST)
        if forms.is_valid():
            print(forms.cleaned_data['name'])
            return HttpResponse('Thanks You Form Submitted !!')
    else:
        forms = ContactForms()
    return render(request , 'myapp/contact.html',{'forms':forms})


#using Class Based Function  Forms used

class ContactClassView(View):

    def get(self,request):
        forms = ContactForms()
        return render(request , 'myapp/contact.html',{'forms':forms})


    def post(self,request):
        forms = ContactForms(request.POST)
        if forms.is_valid():
            print(forms.cleaned_data['name'])
            return HttpResponse('Thanks You Form Submitted !!')