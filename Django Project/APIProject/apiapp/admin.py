from django.contrib import admin
from .models import studInfo

# Register your models here.
class studAdmin(admin.ModelAdmin):
    list_display=['name','sub','email','mobile']

admin.site.register(studInfo,studAdmin)
