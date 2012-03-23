from django.shortcuts import render_to_response

from news.models import NewsItem

def index(request):
    items = NewsItem.objects.order_by('-date')
    return render_to_response('news/index.html', {'items': items})
