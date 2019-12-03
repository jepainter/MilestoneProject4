from django.conf.urls import url, include
from artifacts.views import all_artifacts, view_artifact

# URL patterns to display artifacts
urlpatterns = [
    url(r'^$', all_artifacts, name="artifacts"),
    url(r'^view/(?P<id>\d+)', view_artifact, name="view_artifact"),
]