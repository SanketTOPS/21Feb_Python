from django.shortcuts import render,redirect
from .forms import userForm
from .models import userinfo

# Create your views here.

def index(request):
    if request.method=='POST':
        newuser=userForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Record inserted!")
        else:
            print(newuser.errors)
    return render(request,'index.html')

def showdata(request):
    data=userinfo.objects.all()
    return render(request,'showdata.html',{'data':data})

def updatedata(request,id):
    stid=userinfo.objects.get(id=id)
    if request.method=='POST':
        newuser=userForm(request.POST)
        if newuser.is_valid():
            newuser=userForm(request.POST,instance=stid)
            newuser.save()
            print("Record updated!")
            return redirect('showdata')
        else:
            print(newuser.errors)
    return render(request,'updatedata.html',{'cid':userinfo.objects.get(id=id)})

def deletedata(request,id):
    stid=userinfo.objects.get(id=id)
    userinfo.delete(stid)
    return redirect('showdata')
    