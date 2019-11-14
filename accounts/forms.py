from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserLoginForm(forms.Form):
    """
    Form for user to input info to log in
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """
    Form for new user to input info to register
    """
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]
    
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