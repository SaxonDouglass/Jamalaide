from django.conf.urls.defaults import *

urlpatterns = patterns('jams.views',
    url(r'^$', 'index'),
    url(r'^(?P<jam_url>[\w-]+)$', 'jam'),
)

