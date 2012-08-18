from django.conf.urls.defaults import *

urlpatterns = patterns('pages.views',
    url(r'^$', 'index'),
    url(r'^(?P<slug>[\w-]+)/$', 'page'),
)
