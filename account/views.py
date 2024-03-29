from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import  authenticate,login
from .forms import LoginForm
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request,user)
                return HttpResponse("welcome,you have been successfull")
            else:
                return HttpResponse("sorry,you password is not right")
        else:            return HttpResponse("invalid login")

    if request.method == "GET":
        login_form = LoginForm()
        return render(request,"account/login.html",{"form":login_form})
