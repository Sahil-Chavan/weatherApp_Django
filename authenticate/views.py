from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if Credentials.objects.filter(username=username).exists():
                messages.info(request,'Username is already registered')
                return redirect('/')
            else:        
                data = Credentials(username=username,password=password1)
                data.save()
                messages.info(request,'You have been registered..please login to proceed')
                return redirect("/")
        else:
            messages.info(request,'Password not matching')
            return redirect('/')
    else:
        return render(request,'login.html')

def home(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        if Credentials.objects.filter(username=username).exists():
            user = Credentials.objects.get(username=username)
            if user.password==password:
                request.session['userid']=username
                return redirect('/weather/home')
            else:
                messages.info(request,'Password is not correct')
                return redirect('/')
        else:
            messages.info(request,'Username does not exists')
            return redirect('/')
    else:
        return render(request,'index.html')
        