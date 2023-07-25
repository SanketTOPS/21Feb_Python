from django.contrib import admin
from django.urls import path,include
from apiapp import views

urlpatterns = [
    path('getalldata/',views.getalldata),
    path('getid/<int:id>/',views.getid),
    path('deleteid/<int:id>/',views.deleteid),
    path('savedata/',views.savedata),
    path('updatedata/<int:id>/',views.updatedata),
]
