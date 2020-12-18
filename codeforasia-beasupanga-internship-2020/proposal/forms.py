from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Proposal

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        label = 'Username',
        widget = forms.TextInput(attrs={
            'class': 'form-control username'
        }),
        max_length = 20,
        min_length = 5
    )

    email = forms.EmailField(
        required=True,
        label = 'Email',
        widget = forms.TextInput(attrs = {
            'class':'form-control email'
        }),
        max_length = 100
    )

    password1 = forms.CharField(
        required=True,
        label = 'Password',
        widget = forms.PasswordInput(attrs = {
            'class':'form-control password1',
        }),
    )

    password2 = forms.CharField(
        required=True,
        label = 'Confirm Password',
        widget = forms.PasswordInput(attrs = {
            'class':'form-control password2',
        }),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProjectProposalForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget = forms.TextInput(attrs={
            'class': 'form-control'
        }),
        max_length = 255,
        min_length = 5
    )

    cost = forms.IntegerField(
        required=True,
        widget = forms.NumberInput(attrs={
            'class': 'form-control'
        }),
    )

    about = forms.CharField(
        required=True,
        widget = forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Write a brief description about your project'
        }),
        max_length = 1500,
    )

    class Meta:
        model = Proposal
        fields = ['title', 'cost', 'about']
