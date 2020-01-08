from django.conf.urls import url
from bids.views import (view_bids, add_bid, adjust_bid, remove_bid,
                        view_user_bids, archive_bid)

urlpatterns = [
    url(r'^view/(?P<id>\d+)$', view_bids, name="view_bids"),
    url(r'^add/(?P<id>\d+)$', add_bid, name="add_bid"),
    url(r'^adjust/(?P<id>\d+)$', adjust_bid, name="adjust_bid"),
    url(r'^remove/(?P<id>\d+)$', remove_bid, name="remove_bid"),
    url(r'^view/$', view_user_bids, name="view_user_bids"),
    url(r'^archive/(?P<id>\d+)$', archive_bid, name="archive_bid"),
    ]