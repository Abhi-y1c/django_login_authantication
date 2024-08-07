from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.

def SignupPage(request):

     if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('password1')

        if pass1!=pass2:
            return HttpResponse("your password and confirm password are not same")
        else:
           my_user=User.objects.create_user(uname,email,pass1)
           my_user.save()
           return redirect('login')
        # return HttpResponse("user can be create succesfully")
        # print(uname,email,pass1,pass2)

     return render(request,'signup.html')


def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        # print(username,pass1)
        user=authenticate(request,username=username,password=pass1)
        if user is not None:

            login(request,user)
            return redirect('home')
        # else:
        #     return HttpResponse("username and password is incorect")
    return render(request,'login.html')

def Home(request):
    return render(request,'home.html')