from django.conf.urls import include, patterns, url

urlpatterns = patterns('devs.views',
    url(r'^$', 'devs'),
    url(r'^(?P<slug>[\w-]+)/?$', 'profile'),
)
