from django.conf.urls import include, patterns, url

from accounts.views import *

urlpatterns = patterns('',
    url(r'^profile/?$', profile, {}, "profile"),
    url(r'^profile/update/?$', update, {}, "update_profile"),
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, "login"),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'accounts/logout.html'}, "logout"),
    (r'^password-change/$', 'django.contrib.auth.views.password_change', {'template_name': 'accounts/password-change.html'}, "password_change"),
    (r'^password-change-done/$', 'django.contrib.auth.views.password_change_done', {'template_name': 'accounts/password-change-done.html'}, "password_change_done"),
    (r'^register/$', register, {}, "register"),
    (r'^reset/$', 'django.contrib.auth.views.password_reset', {'template_name': 'accounts/reset-password.html', 'email_template_name': 'accounts/reset-password-email.html'}, "password_reset"),
    (r'^reset/done/$', 'django.contrib.auth.views.password_reset_done', {'template_name': 'accounts/reset-password-done.html'}, "password_reset_done"),
    (r'^reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'template_name': 'accounts/reset-password-confirm.html', 'post_reset_redirect': "profile"}, "password_reset_confirm"),
)
