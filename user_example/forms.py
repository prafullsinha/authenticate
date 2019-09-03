from django import forms
from .models import Index

class IndexForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    dob = forms.DateField()

    class Meta:
          model= Index
          fields=('name','email','dob',)