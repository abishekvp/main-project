from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import User, Group, Permission
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from app.views import db_user
from django.contrib.auth.decorators import user_passes_test
import requests
from bs4 import BeautifulSoup
# Create your views here.

def is_lawyer(user):
    return user.groups.filter(name='lawyer').exists()

@user_passes_test(is_lawyer)
def index(request):
    if request.user.is_authenticated:
        return render(request, 'lawyer/dashboard.html')
    else:return redirect('signin')

@user_passes_test(is_lawyer)
def profile(request):
    return render(request, 'lawyer/profile.html')

@user_passes_test(is_lawyer)
def lawyers(request):
    # lawyers_data = {}
    # for i in db_user.find():
    #     if i['role'] == 'lawyer':
    #         lawyers_data[i['email']] = {
    #             "name":i['name'],
    #             "email":i['email'],
    #             "phone":i['phone'],
    #             "address":i['address'],
    #         }
    return render(request, 'lawyer/lawyers.html')

@user_passes_test(is_lawyer)
def happenings(request):
    url = 'https://economictimes.indiatimes.com/topic/law-and-order'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        contents = soup.find_all('div',class_='contentD')
        image = soup.find_all('div',class_='imgD')
        data={}
        id=0
        for content,img in zip(contents,image):
            title = content.find('a')
            image = img.find('span')
            image = image.find('img')
            description = content.find('div',class_="wrapLines l3")
            data["content"+str(id)] = {
                "image":image.get("src"),
                "title":title.get("title"),
                "description":description.text
            }
            id+=1
        return render(request, 'lawyer/happenings.html',{"data":data})
    else:
        messages.info(request, 'Error in fetching data from the website. Please try again later.')
    return render(request, 'lawyer/happenings.html')

def update_profile(request):
    if request.method=="POST":
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        username = request.POST['username']
        contact = request.POST['contact']
        dob = request.POST['dob']
        expertise = request.POST['expertise']
        email = request.user["email"]
        print(email)
        # db_user.update_one({"email":email},{"$set":{"name":name,"phone":phone,"address":address}})
        messages.info(request, 'Profile updated successfully.')