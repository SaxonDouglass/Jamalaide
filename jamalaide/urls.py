from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^jams/games/?$', 'django.views.generic.simple.direct_to_template',
     {'template': 'games.html'}),
    (r'^jams/agj-1/curse/?$', 'django.views.generic.simple.direct_to_template',
     {'template': 'curse.html'}),
    (r'^jams/agj-1/matt-and-chris/?$', 'django.views.generic.simple.direct_to_template',
     {'template': 'matt-and-chris.html'}),
    (r'^jams/agj-1/operation-cooperation/?$', 'django.views.generic.simple.direct_to_template',
     {'template': 'operation-cooperation.html'}),
    (r'^jams/agj-1/robojam/?$', 'django.views.generic.simple.direct_to_template',
     {'template': 'robojam.html'}),
    (r'^jams/agj-1/rock-guy/?$', 'django.views.generic.simple.direct_to_template',
     {'template': 'rock-guy.html'}),
    (r'^jams/agj-1/some-game-by-james/?$', 'django.views.generic.simple.direct_to_template',
     {'template': 'some-game-by-james.html'}),
    (r'^jams/agj-1/sound-and-vision/?$', 'django.views.generic.simple.direct_to_template',
     {'template': 'sound-and-vision.html'}),
    (r'^jams/agj-1/three-jumping-dudes/?$', 'django.views.generic.simple.direct_to_template',
     {'template': 'three-jumping-dudes.html'}),
    (r'^jams/agj-1/tunnel-experience/?$', 'django.views.generic.simple.direct_to_template',
     {'template': 'tunnel-experience.html'}),
    (r'^jams/agj-1/unamed/?$', 'django.views.generic.simple.direct_to_template',
     {'template': 'unamed.html'}),
    (r'^jams/agj-1/violence-chap/?$', 'django.views.generic.simple.direct_to_template',
     {'template': 'violence-chap.html'}),
    (r'^jams/agj-1/joshs-game/?$', 'django.views.generic.simple.direct_to_template',
     {'template': 'joshs-game.html'}),
    (r'^jams/agj-1/the-game/?$', 'django.views.generic.simple.direct_to_template',
     {'template': 'the-game.html'}),
    (r'^jams/agj-1/?$', 'django.views.generic.simple.direct_to_template',
     {'template': '2011-11-19.html'}),
    url(r'^jams/', include('jams.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('news.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^', include('pages.urls'))
)