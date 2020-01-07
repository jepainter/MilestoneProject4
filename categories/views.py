from django.shortcuts import render
from categories.models import Category
from artifacts.models import Artifact

# Views for the categories in app
def all_categories(request):
    """
    View searches all categories and renders to page.
    """
    
    categories = Category.objects.all()
    
    return render(request, "categories.html", {"categories": categories})


def view_category(request, id):
    """
    View to get one category and associated artifacts, via match with
    category field in artifact. 
    """
    
    artifacts = Artifact.objects.filter(category=id)
    
    return render(request, "artifacts.html", {"artifacts": artifacts})

    