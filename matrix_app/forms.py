from django import forms

class ContactForm(forms.Form):
        name = forms.CharField(max_length=250, required=True)
        email = forms.EmailField(required=True)
        phone = forms.CharField(required=True)
        message = forms.CharField(widget=forms.Textarea, required=True)