from django.shortcuts import render_to_response, get_object_or_404

from forums.models import *

def index(request):
    threads = Thread.objects.order_by('-updated')
    return render_to_response('forums/index.html', {'threads': threads})

def thread(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    posts = Post.objects.filter(thread=thread).order_by('posted')
    return render_to_response('forums/thread.html', {'thread': thread, 'posts': posts})
