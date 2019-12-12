from django.conf.urls import url
from bids.views import view_bids

urlpatterns = [
    url(r'^view/(?P<id>\d+)', view_bids, name="view_bids"),
    ]