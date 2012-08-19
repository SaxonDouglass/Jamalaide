from django.conf.urls.defaults import *

from accounts.views import *

urlpatterns = patterns('',
    url(r'^profile/?$', profile, {}, "accounts-profile"),
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, "accounts-login"),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'accounts/logout.html'}, "accounts-logout"),
    (r'^password-change/$', 'django.contrib.auth.views.password_change', {'template_name': 'accounts/password-change.html'}, "accounts-password-change"),
    (r'^password-change-done/$', 'django.contrib.auth.views.password_change_done', {'template_name': 'accounts/password-change-done.html'}, "accounts-password-change-done"),
)
