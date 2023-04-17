from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile
from django.core.validators import MaxLengthValidator


INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
INPUT_CLASSE_IMAGE = 'w-full py-4 px-6 rounded-xl border bg-white'



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

        username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Your username',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))

        email = forms.CharField(widget=forms.EmailInput(attrs={
            'placeholder': 'Your email address',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))

        password1 = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Your password',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))

        password2 = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat password',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(validators=[MaxLengthValidator(20)], widget=forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'required': True,
                'placeholder': 'Your first name (max 18 letters)',
            }))

    class Meta:
        model = Profile
        fields = ('first_name', 'second_name', 'address', 'email', 'mobile', 'whatsapp', 'image',)

        widgets = {
            'second_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'required': True,
                'placeholder': 'Your first name'
            }),


            'address': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'required': True,
                'placeholder': 'Your second name'
            }),
            'email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES,
                'required': True,
                'placeholder': 'your email address'
            }),
            'mobile': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'required': True,
                'placeholder': 'eg. +243973294723'
            }),
            'whatsapp': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'required': True,
                'placeholder': 'eg. +243813294723'
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSE_IMAGE,
                'required': True,
            }),
        }

        help_texts = {
            'second_name': '<span class="text-teal-500 text-sm">This is your other name or company</span>',
            'address': '<span class="text-teal-500 text-sm">The address of your shop</span>',
            'email': '<span class="text-teal-500 text-sm">Your current email address, if any</span>',
            'mobile': '<span class="text-teal-500 text-sm">The line whereby clients can contact you</span>',
            'whatsapp': '<span class="text-teal-500 text-sm">The line whereby clients can contact you</span>',
            'image': '<span class="text-teal-500 text-sm">This is your profile photo</span>',
        }


