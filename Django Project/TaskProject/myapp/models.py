from django.db import models

# Create your models here.
class userinfo(models.Model):
    Firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    city=models.CharField(max_length=20)
    phone=models.BigIntegerField()