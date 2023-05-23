from django.shortcuts import render,redirect
from .forms import signupForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def usersignup(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")
            return redirect('/')
        else:
            print(newuser.errors)
    return render(request,'usersignup.html')