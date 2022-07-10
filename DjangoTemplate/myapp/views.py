from importlib.resources import contents
from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate,login

def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def login_user(request):
    if request.method=="POST":
        username = request.POST['user']
        password = request.POST['pass']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            mes = 'please enter valid username and password'
            context ={'message':mes}
            return render(request,'login.html',context)
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')