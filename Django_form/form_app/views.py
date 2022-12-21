from django.shortcuts import render
from .forms import UserResgistrationsForm
# Create your views here.

def showFormData(request):
    fm = UserResgistrationsForm(auto_id='user_%s',label_suffix='-', initial={'name': 'Sohail Badeghar'} ) #auto_id='True',auto_id='False',

    # fm = UserResgistrationsForm(label_suffix='-')

    # fm.order_fields(field_order= [ 'email', 'name','phone_no','password']) #  order by rearranging fields

    return render(request,'form_app/userregistartion.html',{'form':fm})  