from django.shortcuts import render
from artifacts.models import Artifact
from categories.models import Category

# Views for the artifacts in app
def all_artifacts(request):
    
    artifacts = Artifact.objects.all()
    categories = Category.objects.all()
    return render(request, "artifacts.html", {"artifacts": artifacts, "categories": categories})

def view_artifact(request, id):
    artifact = Artifact.objects.filter(id)
    print("------")
    print(artifact)
    
    category = Category.objects.filter(artifact.category)
    
    print(category)
    return render(request, "artifacts.html", {"artifacts": artifact, "categories": category})