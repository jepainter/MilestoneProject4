from django.shortcuts import render
from artifacts.models import Artifact

def search_artifacts(request):
    """
    Function to search artifacts in the database
    """
    artifacts = Artifact.objects.filter(name__icontains=request.GET['q'])
    return render(request, "artifacts.html", {"artifacts": artifacts})