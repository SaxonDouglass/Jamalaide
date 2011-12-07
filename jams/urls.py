from django.conf.urls.defaults import *

urlpatterns = patterns('jams.views',
    url(r'^$', 'index'),
    url(r'^games$', 'games'),
    url(r'^games/(?P<game_name>[\w-]+)$', 'game'),
    url(r'^(?P<jam_url>[\w-]+)$', 'jam'),
)

