from django.conf.urls.defaults import *
from django.conf import settings

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    (r'^_ah/warmup$', 'djangoappengine.views.warmup'),
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to',
        {'url': '/static/img/favicon.ico'}),
    (r'^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'news.html'}),
    (r'^games$', 'django.views.generic.simple.direct_to_template',
     {'template': 'games.html'}),
    (r'^jams/2011/11/19/curse$', 'django.views.generic.simple.direct_to_template',
     {'template': 'curse.html'}),
    (r'^jams/2011/11/19/matt-and-chris$', 'django.views.generic.simple.direct_to_template',
     {'template': 'matt-and-chris.html'}),
    (r'^jams/2011/11/19/operation-cooperation$', 'django.views.generic.simple.direct_to_template',
     {'template': 'operation-cooperation.html'}),
    (r'^jams/2011/11/19/robojam$', 'django.views.generic.simple.direct_to_template',
     {'template': 'robojam.html'}),
    (r'^jams/2011/11/19/rock-guy$', 'django.views.generic.simple.direct_to_template',
     {'template': 'rock-guy.html'}),
    (r'^jams/2011/11/19/some-game-by-james$', 'django.views.generic.simple.direct_to_template',
     {'template': 'some-game-by-james.html'}),
    (r'^jams/2011/11/19/sound-and-vision$', 'django.views.generic.simple.direct_to_template',
     {'template': 'sound-and-vision.html'}),
    (r'^jams/2011/11/19/three-jumping-dudes$', 'django.views.generic.simple.direct_to_template',
     {'template': 'three-jumping-dudes.html'}),
    (r'^jams/2011/11/19/tunnel-experience$', 'django.views.generic.simple.direct_to_template',
     {'template': 'tunnel-experience.html'}),
    (r'^jams/2011/11/19/unamed$', 'django.views.generic.simple.direct_to_template',
     {'template': 'unamed.html'}),
    (r'^jams/2011/11/19/violence-chap$', 'django.views.generic.simple.direct_to_template',
     {'template': 'violence-chap.html'}),
    (r'^jams/2011/11/19/joshs-game$', 'django.views.generic.simple.direct_to_template',
     {'template': 'joshs-game.html'}),
    (r'^jams/2011/11/19/the-game$', 'django.views.generic.simple.direct_to_template',
     {'template': 'the-game.html'}),
    (r'^jams$', 'django.views.generic.simple.direct_to_template',
     {'template': 'jams.html'}),
    (r'^jams/upcoming$', 'django.views.generic.simple.direct_to_template',
     {'template': 'upcoming.html'}),
    (r'^jams/2011/11/19$', 'django.views.generic.simple.direct_to_template',
     {'template': '2011-11-19.html'}),
    (r'^jams/2011/12/16$', 'django.views.generic.simple.direct_to_template',
     {'template': '2011-12-16.html'}),
    (r'^jams/2012/01/27$', 'django.views.generic.simple.direct_to_template',
     {'template': '2012-01-27.html'}),
    (r'^jams/2012/01/27/register$', 'jams.views.register'),
    (r'^about$', 'django.views.generic.simple.direct_to_template',
     {'template': 'about.html'}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
