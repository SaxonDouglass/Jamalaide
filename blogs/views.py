from django.template import RequestContext

from django.shortcuts import render_to_response

from blogs.models import Article

def news(request, page=0):
    page=int(page)
    prev_page = None
    next_page = None
    if page > 0:
        prev_page = page - 1
    object_list = Article.objects.order_by('-date')[page*5:(page+1)*5 + 1]
    if len(object_list) > 5:
        object_list = object_list[:5]
        next_page = page + 1
    return render_to_response('blogs/index.html',
                              {'object_list': object_list, 'prev': prev_page, 'next': next_page},
                              context_instance=RequestContext(request))
    
