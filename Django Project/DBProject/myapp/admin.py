from django.contrib import admin
from .models import userinfo

# Register your models here.

class userData(admin.ModelAdmin):
    list_display=['name','email','city','address']

admin.site.register(userinfo,userData)