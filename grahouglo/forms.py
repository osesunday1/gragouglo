from django import forms
from django.forms import ModelForm
from .models import Contact


class ClientForm(ModelForm):
    name = forms.TextInput()
    number= forms.TextInput() 
    email= forms.EmailInput()
    message = forms.TextInput()
    class Meta: 
        model = Contact
        fields= ['name', 'number', 'email', 'message']

        widgets= {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Full Name'}),
            'number': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Phone Number'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email Address'}),
            'message':forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Description'}),

        }