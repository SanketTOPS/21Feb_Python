from django.shortcuts import render
from .models import stdata
from .forms import stdataForm

# Create your views here.
def index(request):
    if request.method=='POST':
        new=stdataForm(request.POST)
        if new.is_valid():
            new.save()
            print("Data Inserted!")
        else:
            print(new.errors)
    return render(request,'index.html')

