from django.conf.urls.defaults import *

urlpatterns = patterns('mailer.views',
    url(r'^$', 'send_mail'),
)
