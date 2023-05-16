from django import forms
from .models import userinfo

class userForm(forms.ModelForm):
    class Meta:
        model=userinfo
        fields='__all__'