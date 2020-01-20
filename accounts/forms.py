from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserLoginForm(forms.Form):
    """
    Form for user to input info to log in
    """
    
    username = forms.CharField(label="Username or Email:")
    password = forms.CharField(label="Password:", widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """
    Form for new user to input info to register
    """
    
    username = forms.CharField(label="Username:")
    email = forms.CharField(label="Email:", widget=forms.EmailInput)
    password1 = forms.CharField(
        label="Password:",
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirm Password:",
        widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")
        
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError("That email address is already taken.")
        
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if not password1 or not password2:
            raise forms.ValidationError("Please confirm your password.")
        
        if password1 != password2:
            raise forms.ValidationError("Your passwords do not match.")
        
        return password2


class ProfileUpdateForm(forms.Form):
    """
    Form for update of user details
    """
    
    username = forms.CharField(
        label="Username:",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "What username do you want to use..."
            })
        )
    email = forms.CharField(
        label="Email:",
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "What email do you want to use..."
            })
        )
    