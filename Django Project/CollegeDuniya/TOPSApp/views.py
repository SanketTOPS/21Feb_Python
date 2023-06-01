from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def errorpage(request):
    return render(request,'404.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def courses(request):
    return render(request,'courses.html')

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,'testimonial.html')