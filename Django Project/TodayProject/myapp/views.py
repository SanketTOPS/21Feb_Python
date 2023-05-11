from django.shortcuts import render
import random

# Create your views here.

def index(request):
    #data={'name':'Hitesh'}
    data={'num':random.randint(1111,9999)}
    #return render(request,'index.html',{'name':'Hitesh'})
    return render(request,'index.html',data)

def about(request):
    return render(request,'about.html')