from django.shortcuts import render,redirect
from .forms import signupForm,updateForm,notesForm,feedbackForm
from .models import userSignup
from django.contrib.auth import logout
from django.core.mail import send_mail
from FinalProject import settings
import requests
import random

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

                #SMS Sending
                otp=random.randint(1111,9999)
                url = "https://www.fast2sms.com/dev/bulkV2"
                querystring = {"authorization":"KEodGZf5czOn3eCxJPkWAFHQUYtS86Rbmrv1MyuViag4hs7N2DujvzKSw5MN9mRryb3LC4DsIHiWph78","variables_values":f"{otp}","route":"otp","numbers":"7777945889,6351472249,6354222979,9824091577,8128970461"}
                headers = {
                    'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)
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
    if request.method=='POST':
        newfeedback=feedbackForm(request.POST)
        if newfeedback.is_valid():
            newfeedback.save()
            print("Your feedback submitted!")

            #Sending Mail
            sub="Thank you!"
            msg=f"Dear User!\n\nWe have recived your feedback, thank you for connecting.\n\nContact on +91 9724799469 | sanket.tops@gmail.com"
            from_id=settings.EMAIL_HOST_USER
            #to_id=['asodariyarutvi@gmail.com','kp21043@gmail.com','naimishramani448@gmail.com','vasiyarabhishek141@gmail.com','preetisharma.1897@gmail.com']
            to_id=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_id,recipient_list=to_id)
        else:
            print(newfeedback.errors)
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