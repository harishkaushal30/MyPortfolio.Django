from django import forms
from django.forms import ModelForm, Textarea, TextInput, EmailInput
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'label':'Your Name', 'placeholder':'Your Name', 'class': 'form-control'}),
            'email_id': EmailInput(attrs={'placeholder': 'Your email address', 'class': 'form-control'}),
            'subject': TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control'}),
            'message': Textarea(attrs={'placeholder': "Your message", 'class': 'form-control'}),
        }