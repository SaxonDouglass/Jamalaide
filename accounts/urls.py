from django.conf.urls import include, patterns, url

from accounts.views import *

urlpatterns = patterns('',
    url(r'^profile/?$', profile, {}, "profile"),
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, "login"),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'accounts/logout.html'}, "logout"),
    (r'^password-change/$', 'django.contrib.auth.views.password_change', {'template_name': 'accounts/password-change.html'}, "password_change"),
    (r'^password-change-done/$', 'django.contrib.auth.views.password_change_done', {'template_name': 'accounts/password-change-done.html'}, "password_change_done"),
)
