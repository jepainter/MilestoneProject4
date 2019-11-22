from django.shortcuts import render
from categories.models import Category

# Views for the categories in app
def all_categories(request):
    
    categories = Category.objects.all()
    return render(request, "categories.html", {"categories": categories})
