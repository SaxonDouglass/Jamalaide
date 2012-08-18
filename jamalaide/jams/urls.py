from django.conf.urls.defaults import *

urlpatterns = patterns('jamalaide.jams.views',
    url(r'^$', 'past'),
    url(r'^upcoming$', 'future'),
    url(r'^(?P<jam_url>[\w-]+)$', 'jam'),
)

