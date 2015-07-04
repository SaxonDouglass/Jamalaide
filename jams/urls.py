from django.conf.urls import include, patterns, url

urlpatterns = patterns('jams.views',
    url(r'^$', 'past'),
    url(r'^upcoming$', 'future'),
    url(r'^(?P<jam_slug>[\w-]+)/?$', 'jam'),
    url(r'^(?P<jam_slug>[\w-]+)/new/?$', 'edit_game'),
    url(r'^(?P<jam_slug>[\w-]+)/(?P<game_slug>[\w-]+)/edit/?$', 'edit_game'),
    url(r'^(?P<jam_slug>[\w-]+)/(?P<game_slug>[\w-]+)/?$', 'game'),
)

