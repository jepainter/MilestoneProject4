from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from accounts.forms import UserLoginForm, UserRegistrationForm, ProfileUpdateForm
from artifacts.models import Artifact

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


@login_required
def update_user_profile(request):
    """
    Update the profile for the logged in user
    """
    
    if request.method == "POST":
        profile_update_form = ProfileUpdateForm(request.POST)
        
        if profile_update_form.is_valid():
            current_user = request.user
            user_email = profile_update_form.cleaned_data["email"]
            user_username = profile_update_form.cleaned_data["username"]
            
            try:
                db_user = User.objects.get(email=user_email)
                if db_user.email == current_user.email:
                    db_user.username = user_username
                    db_user.email = user_email
                    db_user.save()
                    messages.success(request, "Your profile has been updated.")
                    return render(request,'profile.html', {"profile": db_user})
                else:
                    profile_update_form.add_error("email", "Sorry that email is taken by someone else.")
            except:
                try:
                    db_user = User.objects.get(email=current_user.email)
                    db_user.username = user_username
                    db_user.email = user_email
                    db_user.save()
                    messages.success(request, "Your profile has been updated.")
                    return render(request,'profile.html', {"profile": db_user})
                except:
                    messages.error(request, "We were unable to update your details.")
            
        else:
            profile_update_form.add_error(None, "Please check the details.")
    
    else:
        profile_update_form = ProfileUpdateForm(
            initial={"username": request.user.username, "email": request.user.email}
            )
    
    return render(request,'profile_update.html', {"profile_update_form": profile_update_form})