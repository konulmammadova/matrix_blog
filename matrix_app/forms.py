from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ad', 'required':False}),
            'email': forms.EmailInput(attrs={'placeholder': 'email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'telefon'}),
            'message': forms.Textarea(attrs={'placeholder': 'mesaj'}),
        }
