from django.conf.urls import include, patterns, url

urlpatterns = patterns('news.views',
    url(r'^$', 'index'),
)

