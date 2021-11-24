from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label='',
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "asd"

            }
        )
    )

    username = forms.CharField(
        label='',
        max_length=30,
        min_length=5,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "asd"
            }
        )
    )

    password1 = forms.CharField(
        label='',
        max_length=30,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "asd"

            }
        )
    )

    password2 = forms.CharField(
        label='',
        max_length=30,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "asd"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
