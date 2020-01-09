from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .models import RegistrationData
from .forms import RegistrationForm,LoginForm
from django.http.response import HttpResponse

# def index(request):
#     return render(request,'reg.html')

def Registration(request):
    if request.method=='POST':
        rform=RegistrationForm(request.POST)
        if rform.is_valid():
            fname=request.POST.get('firstname')
            lname=request.POST.get('lastname')
            uname=request.POST.get('username')
            pwd=request.POST.get('password')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            gend=rform.cleaned_data.get('gender')
            dob=rform.cleaned_data.get('date_of_birth')
            data=RegistrationData(firstname=fname,lastname=lname,username=uname,
                             password=pwd,email=email,mobile=mobile,gender=gend,date_of_birth=dob)
            data.save()
            return redirect('/login/')
        else:
            return HttpResponse('invalid form')
    else:
        rform=RegistrationForm()
        return render(request,'reg.html',{'rform':rform})


def loginview(request):
    if request.method=='POST':
        lform=LoginForm(request.POST)
        if lform.is_valid():
            unm=request.POST.get('username')
            pwd=request.POST.get('password')
            # usnm=RegistrationData.objects.filter(username=unm)
            # pswd=RegistrationData.objects.filter(password=pwd)
            user=RegistrationData.objects.filter(username=unm,password=pwd)
            if not user:
                return HttpResponse('Login failed')
            else:
                return HttpResponse('Login success')
        else:
            return HttpResponse('user missed some values')
    else:
        lform=LoginForm()
        return render(request,'login.html',{'lform':lform})