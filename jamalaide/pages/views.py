from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from models import *

def index(request):
    return page(request, '__index__')

def page(request, slug):
    p = get_object_or_404(Page, slug=slug)
    return render_to_response('pages/page.html', {'page': p}, context_instance=RequestContext(request))
