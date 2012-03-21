from django.shortcuts import render_to_response, get_list_or_404

from news.models import NewsItem

def index(request):
    items = get_list_or_404(NewsItem, )
    return render_to_response('news/index.html', {'items': items})
