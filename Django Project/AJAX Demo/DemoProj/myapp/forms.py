from django import forms
from .models import stdata


class stdataForm(forms.ModelForm):
    class Meta:
        model=stdata
        fields='__all__'