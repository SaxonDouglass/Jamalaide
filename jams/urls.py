from django.conf.urls import include, patterns, url

urlpatterns = patterns('jams.views',
    url(r'^$', 'past'),
    url(r'^upcoming$', 'future'),
    url(r'^(?P<jam_url>[\w-]+)/?$', 'jam'),
    url(r'^(?P<jam_url>[\w-]+)/new/?$', 'edit_game'),
    url(r'^(?P<jam_url>[\w-]+)/(?P<game_url>[\w-]+)/edit/?$', 'edit_game'),
    url(r'^(?P<jam_url>[\w-]+)/(?P<game_url>[\w-]+)/?$', 'game'),
    url(r'^(?P<jam_url>[\w-]+)/(?P<game_url>[\w-]+)/resource/new/?$', 'edit_res'),
    url(r'^(?P<jam_url>[\w-]+)/(?P<game_url>[\w-]+)/resource/edit/(?P<res_id>[\d-]+)/?$', 'edit_res'),
    url(r'^(?P<jam_url>[\w-]+)/(?P<game_url>[\w-]+)/resource/delete/(?P<res_id>[\d-]+)/?$', 'rm_res'),
)

