from django.conf.urls import url
from bids.views import view_bids, add_bid, adjust_bid

urlpatterns = [
    url(r'^view/(?P<id>\d+)', view_bids, name="view_bids"),
    url(r'^add/(?P<id>\d+)', add_bid, name="add_bid"),
    url(r'^adjust/(?P<id>\d+)', adjust_bid, name="adjust_bid"),
    ]