from django.shortcuts import render
from .forms import UserResgistrationsForm
# Create your views here.

def showFormData(request):
    if request.method == 'POST':
        fm = UserResgistrationsForm(request.POST)
        print("post request")
        if fm.is_valid():
            # first way to get data, Always prefer this way to get data from forms

            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            phone_no = fm.cleaned_data['phone_no']
            password =  fm.cleaned_data['password']

            # Second  way to get data

            # name = request.POST['name']
            # email = request.POST['email']
            # phone_no = request.POST['phone_no']
            # password =  request.POST['password']


            print('Data is valid')
            print('name:',name )
            print('email:', email)
            print('phone_no:', phone_no)
            print('password:',  password )

    else:
        fm = UserResgistrationsForm()
        print('get request')
    return render(request,'myapp/home.html',{'form':fm})  