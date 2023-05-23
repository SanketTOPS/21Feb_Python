from django.db import models
from datetime import datetime

# Create your models here.

class userSignup(models.Model):
    created=models.DateTimeField(default=datetime.now(),blank=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=12)
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    mobile=models.BigIntegerField()
