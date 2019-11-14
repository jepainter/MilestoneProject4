from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm

def index(request):
    """
    Return the index file for the accounts app
    """
    return render(request, "index.html")
    

@login_required    
def logout(request):
    """
    Return index page after user logged out, provide message on success,
    prevent redirect to logout page if user already logged out
    """
    auth.logout(request)
    messages.success(request, "You have been logged out.")
    return redirect(reverse("index"))


def login(request):
    """
    Return login page, provide message on success and redirect to index page,
    prevent redirect to login page if already logged in
    """
    if request.user.is_authenticated:
        return redirect(reverse("index"))
        
    if request.method =="POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST["username"],
                                     password=request.POST["password"])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have been logged in.")
                return redirect(reverse("index"))
            else:
                login_form.add_error(None, "The username or password is incorrect.")
    
    else:
        login_form = UserLoginForm()
        
    return render(request, "login.html", {"login_form": login_form})


def registration(request):
    """
    Return the registration page to create a new user
    """
    if request.user.is_authenticated:
        return redirect(reverse("index"))
    
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            user = auth.authenticate(username=request.POST["username"],
                                     password=request.POST["password1"])
                                     
            if user:
                auth.login(user=user, request=request)
                messages.success(
                    request,
                    "You have been registered and logged in.")
                return redirect(reverse("index"))
            else:
                messages.error(
                    request,
                    "We are not able to register your account at this time.")
    
    else:
        registration_form = UserRegistrationForm()
    return render(request, "registration.html", {
        "registration_form": registration_form})


@login_required
def user_profile(request):
    """
    Return the profile fo the logged in user
    """
    user = User.objects.get(email=request.user.email)
    return render(request,'profile.html', {"profile": user})