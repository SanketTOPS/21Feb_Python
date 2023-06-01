from django.contrib import admin
from django.urls import path,include
from TOPSApp import views

urlpatterns = [
    path('',views.index),
    path('errorpage/',views.errorpage),
    path('about/',views.about),
    path('contact/',views.contact),
    path('courses/',views.courses),
    path('team/',views.team),
    path('testimonial/',views.testimonial),
]
