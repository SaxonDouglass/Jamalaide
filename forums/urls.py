from django.conf.urls.defaults import *

urlpatterns = patterns('forums.views',
    url(r'^$', 'index'),
    url(r'^thread/(?P<thread_id>[\w-]+)$', 'thread'),
)

