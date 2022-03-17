from  django.contrib.auth.forms import UsernameField,AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django import forms

class RegistrationForm(forms.Form):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True,'id':"forUsrnameInput",'class':"form-control"}),
        required=True
    )
    email = forms.CharField(
        strip=False,
        widget=forms.TextInput(attrs={"autocomplete": "current-password","id":"forEmailInput","type":"email",'class':"form-control"}),required=True,validators=[EmailValidator]
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password","id":"forPassword1Input",'class':"form-control",'type':"password"}),required=True,min_length=8
    )
    password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password","id":"forPassword2Input",'class':"form-control",'type':"password"}),required=True
    )   
    class Meta:
        model = User
        fields = ("username","email","password")