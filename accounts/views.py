from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm

def index(request):
    """
    Return the index file for the accounts app
    """
    return render(request, "index.html")
    

@login_required    
def logout(request):
    """
    Return index page after user logged out, provide message on success
    """
    auth.logout(request)
    messages.success(request, "You have been logged out.")
    return redirect(reverse("index"))


def login(request):
    """
    Return login page, provide message on success
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