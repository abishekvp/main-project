from django.db import models

class User(models.Model):
    username = models.CharField(max_length=32, unique=True)
    email = models.EmailField(max_length=32, unique=True)
    role = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    
