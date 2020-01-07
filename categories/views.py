from django.shortcuts import render, redirect
from categories.models import Category
from artifacts.models import Artifact

# Views for the categories in app
def all_categories(request):
    """
    View searches all categories and renders to page_heading
    """
    
    categories = Category.objects.all()
    return render(request, "categories.html", {"categories": categories})

def view_category(request, id):
    """
    View to get one category and associated artifacts and render html
    
    CHANGE function to only search artifacts and not categories
    """
    
    category = Category.objects.filter(id=id)
    print("")
    print("## Inside single category function ##")
    print("Category: " + str(category))
    
    for category_detail in category:
        
        print("Category ID: " + str(category_detail.id))
        print("Category Name: " + str(category_detail.category_name))
        print("Category Description: " + str(category_detail.category_description))
    
    artifacts = Artifact.objects.filter(category=category_detail.id)
    
    print("Artifacts: " + str(artifacts))
    
    return render(request, "artifacts.html", {"artifacts": artifacts})
    
def add_category(request):
    """
    Function to add a category in the database if the user is a superuser
    """
    
    
    