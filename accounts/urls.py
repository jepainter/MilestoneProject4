from django.conf.urls import url, include
from accounts.views import index, logout, login, registration, user_profile, update_user_profile
from accounts import urls_password_reset

#URL's for rendering of account views
urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="register"),
    url(r'^profile/$', user_profile, name="profile"),
    url(r'^update_profile/$', update_user_profile, name="update_user_profile"),
    url(r'^password_reset/', include(urls_password_reset))
]