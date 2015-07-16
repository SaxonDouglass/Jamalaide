from django.conf.urls import include, patterns, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('blogs.urls')),
    url(r'^news/', include('blogs.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^jams/', include('jams.urls')),
    url(r'^games/?$', 'jams.views.games'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
      'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
      'document_root': settings.STATIC_ROOT,
    }),
)

# Flatpages
urlpatterns += patterns('django.contrib.flatpages.views',
    (r'^(?P<url>.*/)$', 'flatpage')
)
