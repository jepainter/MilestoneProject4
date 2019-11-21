from django.conf.urls import url
from search.views import search_artifacts

urlpatterns = [
    url(r'^$', search_artifacts, name="search")
]