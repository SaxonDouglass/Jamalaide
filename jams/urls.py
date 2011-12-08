from django.conf.urls.defaults import *

urlpatterns = patterns('jams.views',
    url(r'^$', 'index'),
    url(r'^(?P<jam_url>[\w-]+)/(?P<game_url>[\w-]+)$', 'game'),
    url(r'^(?P<jam_url>[\w-]+)$', 'jam'),
)

