import re
from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm,EditUserProfileForm,EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
# sign_up View for user sign_up function

def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'your account has been signed up successfully!')
            fm.save()

    else:
        fm = SignUpForm()
    return render(request, 'myapp/Sign_up.html',{'forms':fm})


# login View for user login function
def User_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request = request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,"logged in successfully!")
                    return HttpResponseRedirect('/User_profile/')
        else:      
            fm = AuthenticationForm()
        return render(request, 'myapp/User_login.html',{'forms':fm})
    else:
        return HttpResponseRedirect('/User_profile/')


# profile Update/Edit View for user profile function

def User_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST, instance = request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(request.POST,instance=request.user)
                users = None
            if fm.is_valid():
                messages.success(request, 'User profile has been updated successfully!')
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(instance=request.user)
                users = None
        return render(request, 'myapp/User_profile.html',{'name':request.user.username,'forms':fm,'users':users})   
    else:
        return HttpResponseRedirect('/login/')


#logout View for user logout function

def User_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')



#Change password with old password for user profile function

def ChangePassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request,'Password Change Successfully')
                return HttpResponseRedirect('/User_profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'myapp/change_password.html',{'forms':fm})
    else:
        return HttpResponseRedirect('/login/')



def user_details(request ,id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = EditAdminProfileForm(instance=pi)
        return render(request, 'myapp/user_details.html',{'forms':fm})

    else:
        return HttpResponseRedirect('/login/')


