from django.conf.urls.defaults import *

urlpatterns = patterns('jams.views',
    url(r'^$', 'index'),
    url(r'^image/(?P<pk>.+)$', 'download_image'),
    url(r'^source/(?P<pk>.+)$', 'download_source'),
    url(r'^game/(?P<pk>.+)$', 'download_game'),
    url(r'^(?P<jam_url>[\w-]+)/submit$', 'submit'),
    url(r'^(?P<jam_url>[\w-]+)/(?P<game_url>[\w-]+)$', 'game'),
    url(r'^(?P<jam_url>[\w-]+)$', 'jam'),
)

