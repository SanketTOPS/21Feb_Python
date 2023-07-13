from django import forms
from .models import userinfo

class userform(forms.ModelForm):
    class Meta:
        model=userinfo
        fields='__all__'