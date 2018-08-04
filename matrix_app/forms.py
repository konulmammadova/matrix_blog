from django import forms
from .models import Contact, Post
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ad',}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon'}),
            'message': forms.Textarea(attrs={'placeholder': 'Mesajınız'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'İstifadəçi adı', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Şifrə', 'class': 'form-control'}))


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Ad', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Soyad', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'placeholder': 'İstifadəçi adı', 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Şifrə', 'class': 'form-control'}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'sub_title', 'content', 'publish_date', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Başlıq', 'class': 'form-control'}),
            'sub_title': forms.TextInput(attrs={'placeholder': 'Alt başlıq', 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'placeholder': 'Məqalə mətni', 'class': 'form-control', 'type':'datetime-local'}),
            'publish_date': forms.DateInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }

        labels = {
            "title": "Başlıq",
            "sub_title": "Alt başlıq",
            "status": "Status",
        }