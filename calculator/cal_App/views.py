from ast import Num
from django.shortcuts import render

# Create your views here.

def calculator(request):
    Num1 = ""
    Num2 = ""
    Result = ""
    if request.method == 'POST':
        Num1 = int(request.POST.get('Num1'))
        Num2 = int(request.POST.get('Num2'))
    

    return render(request, 'cal_App/calculator.html', {'Num1': Num1, 'Num2': Num2,'Result': Result})
    