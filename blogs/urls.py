from django.conf.urls import include, patterns, url

from blogs.views import ArticleList

urlpatterns = patterns('blogs.views',
    url(r'^$', ArticleList.as_view()),
)
