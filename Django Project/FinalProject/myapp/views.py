from django.shortcuts import render,redirect
from .forms import signupForm,updateForm,notesForm
from .models import userSignup
from django.contrib.auth import logout

# Create your views here.
def index(request):
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("Signup Successfully!")
            else:
                print(newuser.errors)
        elif request.POST.get('login')=='login':

            unm=request.POST['username']
            pas=request.POST['password']
            userid=userSignup.objects.get(username=unm)
            print("ID:",userid.id)

            user=userSignup.objects.filter(username=unm,password=pas)
            if user: #true
                print("Login Successfully!")
                request.session['user']=unm #create a session
                request.session['userid']=userid.id
                return redirect('notes')
            else:
                print("Error!Login Faild...")
    return render(request,'index.html')

def notes(request):
    user=request.session.get('user')
    if request.method=='POST':
        newnotes=notesForm(request.POST,request.FILES)
        if newnotes.is_valid():
            newnotes.save()
            print("Your notes has been uploaded!")
        else:
            print(newnotes.errors)
    return render(request,'notes.html',{'user':user})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def profile(request):
    user=request.session.get('user')
    userid=request.session.get('userid')
    cuser=userSignup.objects.get(id=userid)
    if request.method=='POST':
        updateuser=updateForm(request.POST)
        if updateuser.is_valid():
            updateuser=updateForm(request.POST,instance=cuser)
            updateuser.save()
            print("Your profile has been updated!")
            #return redirect('notes')
            userlogout(request)
            return redirect('/')
        else:
            print(updateuser.errors)
    return render(request,'profile.html',{'user':user,'cuser':userSignup.objects.get(id=userid)})

def userlogout(request):
    logout(request)
    return redirect('/')