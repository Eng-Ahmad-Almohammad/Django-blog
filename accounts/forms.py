from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms

from .models import CustomUser
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name','password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__( *args, **kwargs)
        self.fields["email"].widget.attrs["class"] = "input"
        self.fields["email"].widget.attrs["placeholder"] = "example@example.com"
        self.fields["first_name"].widget.attrs["class"] = "input"
        self.fields["first_name"].widget.attrs["placeholder"] = "Example"
        self.fields["last_name"].widget.attrs["class"] = "input"
        self.fields["last_name"].widget.attrs["placeholder"] = "Example"
        self.fields["password1"].widget.attrs["class"] = "input"
        self.fields["password1"].widget.attrs["placeholder"] = "Your Password"
        self.fields["password2"].widget.attrs["class"] = "input"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"


class SignInForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__( *args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'input'
        self.fields['email'].widget.attrs['placeholder'] = 'example@example.com'
        self.fields['password'].widget.attrs['class'] = 'input'
        self.fields['password'].widget.attrs['placeholder'] = 'Your Password'
