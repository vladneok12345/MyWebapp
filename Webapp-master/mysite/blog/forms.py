from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment
from .models import Trip
from django.core.validators import ValidationError

class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name","email","body")


class SearchForm(forms.ModelForm):
    tags = forms.CharField(label="Tags", max_length=255, help_text="Enter one or more tags, separated by commas")

    class Meta:
        model = Trip
        fields = ("name", "tags", "description")

class RegistrationForm(UserCreationForm):
    email = forms.CharField(max_length=30,label="email", required=True, help_text="Обов'язкове поле", widget=forms.TextInput(attrs={
        'placeholder': 'Enter your email address',
        "id": "inputEmail",
        "class": "form",
    }))
    first_name = forms.CharField(max_length=30, required=True, help_text="Обов'язкове поле", widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"login",
        "id":"inputFirstName",

    }))
    last_name = forms.CharField(max_length=30, required=True, help_text="Обов'язкове поле", widget=forms.TextInput(attrs={
        "id":"inputLastName",
        "class":"form-control",
        "placeholder":"login",
    }))

    class Meta:
        model = User
        fields = [
            'username','email', 'first_name',
            'last_name', 'password1', 'password2'
        ]

        def __init__(self, *args, **kwargs):
            super(RegistrationForm).__init__(*args, **kwargs)
            self.fields['username'].help_texts = "Обов'язкове поле тільки букви, цифри та символи @/./+/-/_."
            self.fields['password1'].help_texts = "Обов'язково використовувати букви та цифри"
            self.fields['password2'].help_texts = "Повторіть ще раз свій пароль"

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={
        "id":"inputLogin",
        "class":"form-control",
        "placeholder":"login",
    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        "type": "password",
        "id":"inputPassword",
        "class":"form-control",
        "placeholder":"0000",
    }))