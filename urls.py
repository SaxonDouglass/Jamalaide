from django.conf.urls.defaults import *
from django.conf import settings

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'news.html'}),
    ('^games$', 'django.views.generic.simple.direct_to_template',
     {'template': 'games.html'}),
    ('^games/matt-and-chris$', 'django.views.generic.simple.direct_to_template',
     {'template': 'matt-and-chris.html'}),
    ('^jams$', 'django.views.generic.simple.direct_to_template',
     {'template': 'jams.html'}),
    ('^jams/upcoming$', 'django.views.generic.simple.direct_to_template',
     {'template': 'upcoming.html'}),
    ('^jams/2011-11-19$', 'django.views.generic.simple.direct_to_template',
     {'template': '2011-11-19.html'}),
    ('^jams/2011-12-16$', 'django.views.generic.simple.direct_to_template',
     {'template': '2011-12-16.html'}),
    ('^jams/2012-01-27$', 'django.views.generic.simple.direct_to_template',
     {'template': '2012-01-27.html'}),
    ('^about$', 'django.views.generic.simple.direct_to_template',
     {'template': 'about.html'}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
