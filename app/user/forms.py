from django.contrib.auth.forms import UsernameField, AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django import forms
from django.contrib.auth.hashers import Argon2PasswordHasher, BasePasswordHasher


class RegistrationForm(forms.Form):
    username = UsernameField(
        label="Your name",
        widget=forms.TextInput(
            attrs={"autofocus": True, "id": "forUsrnameInput", "class": "form-control"}
        ),
        required=True,
    )
    email = forms.CharField(
        label="Email",
        strip=False,
        widget=forms.TextInput(
            attrs={
                "autocomplete": "current-password",
                "id": "forEmailInput",
                "type": "email",
                "class": "form-control",
            }
        ),
        required=True,
        validators=[EmailValidator],
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "id": "forPasswordInput",
                "class": "form-control",
                "type": "password",
            }
        ),
        required=True,
    )
    password2 = forms.CharField(
        label="Repeat password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "id": "forPassword2Input",
                "class": "form-control",
                "type": "password",
            }
        ),
        required=True,
    )

    def clean_username(self):
        cd = self.cleaned_data
        user = User.objects.filter(username=cd.get("username", None))
        if user.exists():
            raise forms.ValidationError("Username alredy exist")
        return cd.get("username")

    def clean_email(self):
        cd = self.cleaned_data
        user = User.objects.filter(email=cd.get("email", None))
        if user.exists():
            raise forms.ValidationError("Email alredy exist")
        return cd.get("email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match.")
        salt = BasePasswordHasher().salt()
        encode_password = Argon2PasswordHasher().encode(cd.get("password2", None), salt)
        return encode_password

    class Meta:
        model = User
        fields = ("username", "email", "password")


class SingInForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "id": "forUsrnameInput",
                "class": "form-control",
                "placeholder": "username or email",
            }
        ),
        required=True,
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "id": "forPasswordInput",
                "class": "form-control",
                "type": "password",
                "placeholder": "password",
            }
        ),
        required=True,
    )

    class Meta:
        model = User
        fields = ("username", "email", "password")

    def clean(self):
        cd = super(SingInForm, self).clean()
        form_password = cd.get("password", None)
        user_password_dict = (
            User.objects.filter(username=cd.get("username", None))
            .values("password")
            .get()
        )
        is_correct = Argon2PasswordHasher().verify(
            form_password, user_password_dict["password"]
        )
        if not is_correct:
            raise forms.ValidationError("password don't match")
        return cd
