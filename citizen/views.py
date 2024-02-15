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

def is_citizen(user):
    return user.groups.filter(name='citizen').exists()    

@user_passes_test(is_citizen)
def index(request):
    if request.user.is_authenticated:
        return render(request, 'citizen/dashboard.html')
    else:return redirect('signin')

@user_passes_test(is_citizen)
def profile(request):
    return render(request, 'citizen/profile.html')

@user_passes_test(is_citizen)
def lawyers(request):
    return render(request, 'citizen/lawyers.html')

@user_passes_test(is_citizen)
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
        return render(request, 'citizen/happenings.html',{"data":data})
            
    else:
        messages.info(request, 'Error in fetching data from the website. Please try again later.')
    return render(request, 'citizen/happenings.html')
