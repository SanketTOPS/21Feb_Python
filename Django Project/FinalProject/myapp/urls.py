from django.contrib import admin
from django.urls import path,include
from myapp import views


urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about),
    path('contact/',views.contact),
    path('profile/',views.profile),
    path('notes/',views.notes,name='notes'),
    path('userlogout/',views.userlogout),
]
