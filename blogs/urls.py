from django.conf.urls import include, patterns, url

from blogs.views import news

urlpatterns = patterns('blogs.views',
    url(r'^$', news),
    url(r'^(?P<page>[0-9]+)/?$', news),
)
