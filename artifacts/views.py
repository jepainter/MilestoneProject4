from django.shortcuts import render
from artifacts.models import Artifact
from categories.models import Category

# Views for the artifacts in app
def all_artifacts(request):
    
    artifacts = Artifact.objects.all()
    categories = Category.objects.all()
    return render(request, "artifacts.html", {"artifacts": artifacts, "categories": categories})

def view_artifact(request, id):
    artifact = Artifact.objects.filter(id=id)
    print("------")
    print("## Inside the view artifact function ##")
    print("Artifact: " + str(artifact))
    for artifact_detail in artifact:
        print("Artifact Name: " + str(artifact_detail.name))
        print("Artifact Id: " + str(artifact_detail.id))
        print("Category Id: " + str(artifact_detail.category))
    
    category = Category.objects.filter(category_name=artifact_detail.category)
    #categories = Category.objects.all()
    
    print("Category: " + str(category))
    
    return render(request, "artifact_detail.html", {"artifact": artifact, "category": category})