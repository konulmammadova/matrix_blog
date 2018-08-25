# from betterforms.multiform import MultiModelForm
from django import forms
from .models import Contact, Post, Profile
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget


# class DateInput(forms.DateInput):
#     input_type = 'date'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ad', }),
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
        fields = ['title', 'image', 'sub_title', 'content', 'publish_date', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Başlıq', 'class': 'form-control'}),
            # 'image': forms.FileInput(attrs={'placeholder': 'Örtük şəkli', 'class': 'form-control'}),
            'sub_title': forms.TextInput(attrs={'placeholder': 'Alt başlıq', 'class': 'form-control'}),
            'content': forms.Textarea(
                attrs={'placeholder': 'Məqalə mətni', 'class': 'form-control', 'type': 'datetime-local'}),
            'publish_date': forms.DateInput(attrs={'class': 'form-control'}),
        }

        labels = {
            "title": "Başlıq",
            "image": "Örtük şəkli",
            "sub_title": "Alt başlıq",
            "status": "Status",
        }


    publish_date = forms.DateField(input_formats=['%m/%d/%Y'])


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Adınız', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Soyadınız', 'class': 'form-control'})
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture', 'about']
        widgets = {
            'picture': forms.FileInput(attrs={'placeholder': 'Profil şəkli', 'class': 'form-control'}),
            'about': forms.Textarea(attrs={'placeholder': 'Haqqımda', 'class': 'form-control'})
        }


# class UserProfileMultiForm(MultiModelForm):
#     form_classes = {
#         'user': UserForm,
#         'profile': ProfileForm,
#     }

