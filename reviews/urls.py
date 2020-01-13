from django.conf.urls import url
from reviews.views import add_review

# URL patterns to display reviews
urlpatterns = [
    url(r'^add/(?P<id>\d+)$', add_review, name="add_review"),
]