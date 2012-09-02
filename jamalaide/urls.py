from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^jams/', include('jams.urls')),
    url(r'^games/?$', 'jams.views.games'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
      'document_root': settings.MEDIA_ROOT,
    }),    
    url(r'^$', include('news.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^', include('pages.urls'))
)
