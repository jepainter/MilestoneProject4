from django.conf.urls import url
from cart.views import view_cart, add_to_cart, adjust_cart, remove_item_from_cart, add_bid_to_cart, remove_bid_from_cart

urlpatterns = [
    url(r'^$', view_cart, name="view_cart"),
    url(r'^add/(?P<id>\d+)', add_to_cart, name="add_to_cart"),
    url(r'^add_bid/(?P<id>\d+)', add_bid_to_cart, name="add_bid_to_cart"),
    url(r'^adjust/(?P<id>\d+)', adjust_cart, name="adjust_cart"),
    url(r'^remove_item/(?P<id>\d+)', remove_item_from_cart, name="remove_item_from_cart"),
    url(r'^remove_bid/(?P<id>\d+)', remove_bid_from_cart, name="remove_bid_from_cart"),
]