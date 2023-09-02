from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated:return redirect("dashboard")
    else:return redirect('signin')

def dashboard(request):
    if request.user.is_authenticated:return render(request,'dashboard.html')
    else:return redirect('signin')

def signup(request):
    if request.user.is_authenticated:return render(request,'index.html')
    elif request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect("dashboard")
    else:return render(request,'signup.html')

def signin(request):
    if request.user.is_authenticated:return render(request,'index.html')
    elif request.method == 'POST':    
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect("dashboard")
    else:return render(request,'signin.html')

def signout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('signin')