from django.shortcuts import render
from artifacts.models import Artifact

# Views for the artifacts in app
def all_artifacts(request):
    artifacts = Artifact.objects.all()
    return render(request, "artifacts.html", {"artifacts": artifacts})
