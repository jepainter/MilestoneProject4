from django.conf.urls import url, include
from artifacts.views import all_artifacts

urlpatterns = [
    url(r'^$', all_artifacts, name="artifacts")
]