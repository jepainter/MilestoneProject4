from django.conf.urls import url
from histories.views import view_history, add_history_event

# URL patterns to display history
urlpatterns = [
    url(r'^view/(?P<id>\d+)$', view_history, name="view_history"),
    url(r'^add/(?P<id>\d+)$', add_history_event, name="add_history_event"),
]