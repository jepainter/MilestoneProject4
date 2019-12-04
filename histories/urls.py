from django.conf.urls import url, include
from histories.views import view_history

# URL patterns to display history
urlpatterns = [
    url(r'^view/(?P<id>\d+)', view_history, name="view_history")
]