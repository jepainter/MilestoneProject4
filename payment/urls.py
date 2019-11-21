from django.conf.urls import url
from payment.views import payment

# URL for rendering view
urlpatterns = [
    url(r'^$', payment, name="payment"),
    ]