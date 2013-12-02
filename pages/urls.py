from django.conf.urls import include, patterns, url

urlpatterns = patterns('pages.views',
    url(r'^$', 'index'),
    url(r'^(?P<slug>[\w-]+)/$', 'page'),
)
