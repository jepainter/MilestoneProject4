"""artifacthunters URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views import static
from artifacthunters.settings import MEDIA_ROOT
from accounts.views import index
from accounts import urls as accounts_urls
from artifacts.views import all_artifacts
from artifacts import urls as artifacts_urls

# URL's for rendering views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^artifacts/', include(artifacts_urls)),
    url(r'^media/(?P<path>.*)$', static.serve, {"document_root": MEDIA_ROOT}),
]
