from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Abishek:<password>@cluster0.edxis.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))

database = client['main-project']
db_users = database['users']

def index(request):
    if request.user.is_authenticated:return redirect("dashboard")
    else:return redirect('signin')

def dashboard(request):
    if request.user.is_authenticated:return render(request,'./user/dashboard.html')
    else:return redirect('signin')


def signup(request):
    if request.user.is_authenticated:return render(request,'index.html')
    elif request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']
        if db_users.find_one(filter={'email':email,'password':password}):messages.info(request, 'Username and Email already exists')
        elif User.objects.filter(username=username).exists():messages.info(request, 'Username already exists')
        elif User.objects.filter(email=email).exists():messages.info(request, 'Email already exists')
        else:
            user = User.objects.create_user(username, email, password)
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("dashboard")
        return redirect("signup")
    else:return render(request,'./sign/signup.html')

# def signup(request):
#     if request.user.is_authenticated:return render(request,'index.html')
#     elif request.method=="POST":
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         if User.objects.filter(username=username).exists() and User.objects.filter(email=email).exists():messages.info(request, 'Username and Email already exists')
#         elif User.objects.filter(username=username).exists():messages.info(request, 'Username already exists')
#         elif User.objects.filter(email=email).exists():messages.info(request, 'Email already exists')
#         else:
#             user = User.objects.create_user(username, email, password)
#             user = authenticate(request, username=username, password=password)
#             login(request, user)
#             return redirect("dashboard")
#         return redirect("signup")
#     else:return render(request,'./sign/signup.html')

def signin(request):
    if request.user.is_authenticated:return render(request,'index.html')
    elif request.method == 'POST':    
        username = request.POST["username"]
        password = request.POST["password"]
        if '@' in username:username = User.objects.get(email=username.lower()).username
        user = authenticate(request, username=username, password=password)
        if user:login(request, user)
        else:messages.info(request, 'User not found')
        return redirect("signin")
    else:return render(request,'./sign/signin.html')

def signout(request):
    if request.user.is_authenticated:logout(request)
    return redirect('signin')