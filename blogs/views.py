from django.views.generic import ListView

from blogs.models import Article

class ArticleList(ListView):
    queryset = Article.objects.order_by('-date')[:5]
    template_name = 'blogs/index.html'
