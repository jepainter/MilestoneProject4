from django.conf.urls import url
from categories.views import all_categories, view_category

# URL patterns to display categories
urlpatterns = [
    url(r'^$', all_categories, name="categories"),
    url(r'^view/(?P<id>\d+)$', view_category, name="view_category")
]