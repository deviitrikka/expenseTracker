from django.shortcuts import render , redirect , HttpResponse
from expense_tracker.models import *
from django.contrib import messages
from django.db.models import Sum

# Create your views here.
def register(request):
    return render(request , 'register.html')

def regi(request):
    name = request.GET['user_name']
    email = request.GET['user_email']
    password = request.GET['user_pass']

    if user.objects.filter(email= email).exists():
        data = {'email' :email , 'message' : "User Already exists Please Login "}
        return render(request , 'login.html' , {'data' : data})

    u = user()
    u.name = name 
    u.email = email
    u.password = password
    u.save()
    k = user.objects.get(email = email)
    return render(request, 'welcome.html' , {'u':k})

def login(request):
    return render(request , 'login.html')

def logi(request):
    email = request.GET['user_email']
    password = request.GET['user_pass']
    if(user.objects.filter(email = email , password = password)):
        u = user.objects.get(email = email)
        return render(request, 'welcome.html' , {'u' :u})
    data = {'message' : "wrong pass or no user exists"}
    return render(request , 'login.html' , {'data' : data})

def show(request ):
    u = user.objects.all()
    return render(request , 'show.html' , {'db':u})
