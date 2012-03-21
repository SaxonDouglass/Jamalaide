from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    url(r'^jams/', include('jams.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('news.urls')),
)

