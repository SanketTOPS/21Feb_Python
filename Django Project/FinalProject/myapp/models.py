from django.db import models
from datetime import datetime

# Create your models here.

class userSignup(models.Model):
    created=models.DateTimeField(default=datetime.now(),blank=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    mobile=models.BigIntegerField()

class mynotes(models.Model):
    created=models.DateTimeField(default=datetime.now(),blank=True)
    title=models.CharField(max_length=100)
    option=models.CharField(max_length=100)
    files=models.FileField(upload_to='myFiles')
    desc=models.TextField()

class feedback(models.Model):
    created=models.DateTimeField(default=datetime.now(),blank=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    msg=models.TextField()

