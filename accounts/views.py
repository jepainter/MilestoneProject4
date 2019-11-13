from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Return the index file for the accounts app
    """
    
    return render(request, "index.html")