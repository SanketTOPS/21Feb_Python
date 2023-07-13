from django.shortcuts import render,redirect
from .forms import userform
from .models import userinfo

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        newuser=userform(request.POST)
        if newuser.is_valid():
            newuser.save()
        else:
            print(newuser.errors)
    return render(request,'signup.html')
    
def login(request):
     if request.method=='POST':
         unm=request.POST['username']
         phone=request.POST['phone']
         new=userinfo.objects.filter(username=unm,phone=phone)
         
         if new :
           request.session['user']=unm
           return redirect ('index') 
         else :
           print('erropr') 
     return render(request,'login.html')   
          
         
         
     