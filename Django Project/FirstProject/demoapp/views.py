from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("This is my first page!")
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')