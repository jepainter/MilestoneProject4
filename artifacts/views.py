from django.shortcuts import render
from artifacts.models import Artifact
#from categories.models import Category

# Views for the artifacts in app
def all_artifacts(request):
    
    artifacts = Artifact.objects.all()
#    categories = Category.objects.all()
    return render(request, "artifacts.html", {"artifacts": artifacts})

def view_artifact(request, id):
    artifact = Artifact.objects.filter(id=id)
    print("------")
    print("## Inside the view artifact function ##")
    print("Artifact: " + str(artifact))
    for artifact_detail in artifact:
        print("Artifact Name: " + str(artifact_detail.name))
        print("Artifact Id: " + str(artifact_detail.id))
        print("Category Object: " + str(artifact_detail.category))
        print("Category Id: " + str(artifact_detail.category.id))
        print("Category Description: " + str(artifact_detail.category.category_description))
    
    #category = Category.objects.filter(category_name=artifact_detail.category)
    #categories = Category.objects.all()
    
    print("")
    print("Testing access from artifact to category via foreignkey")
    print("Artifact: " + str(artifact))
    
    
    print("Exit test")
    print("")
    
    
    #print("Category: " + str(category))
    
    return render(request, "artifact_detail.html", {"artifact": artifact})