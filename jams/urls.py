from django.conf.urls.defaults import *

urlpatterns = patterns('jams.views',
    url(r'^$', 'past'),
    url(r'^upcoming$', 'future'),
    url(r'^(?P<jam_url>[\w-]+)$', 'jam'),
    url(r'^(?P<jam_url>[\w-]+)/submit$', 'submit'),
    url(r'^(?P<jam_url>[\w-]+)/(?P<game_url>[\w-]+)$', 'game'),
)

