from django.conf.urls import url, include
from categories.views import all_categories

# URL patterns to display categories
urlpatterns = [
    url(r'^$', all_categories, name="categories")
]