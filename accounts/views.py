from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

def index(request):
    """
    Return the index file for the accounts app
    """
    return render(request, "index.html")
    
    
def logout(request):
    """
    Log out of the user and redirect to index page
    """
    auth.logout(request)
    messages.success(request, "You have been logged out.")
    return redirect(reverse("index"))