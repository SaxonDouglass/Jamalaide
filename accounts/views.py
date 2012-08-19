from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect

def profile(request):
    if request.user:
        return render_to_response('accounts/profile.html',{},
          context_instance=RequestContext(request))
