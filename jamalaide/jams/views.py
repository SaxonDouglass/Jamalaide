import datetime
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from jamalaide.jams.models import Jam

def future(request):
    jams = Jam.objects.filter(end__gt=datetime.datetime.now()).order_by('end')
    return render_to_response('jams/index.html',
                              {'jams': jams, 'title': "Upcoming Jams"},
                              context_instance=RequestContext(request))

def past(request):
    jams = Jam.objects.filter(end__lt=datetime.datetime.now()).order_by('-end')
    return render_to_response('jams/index.html',
                              {'jams': jams, 'title': "Jams"},
                              context_instance=RequestContext(request))

def jam(request, jam_url):
    jam = get_object_or_404(Jam, url=jam_url)
    duration = jam.end-jam.start
    hours = duration.days*24 + duration.seconds/3600
    minutes = duration.seconds%3600/60
    return render_to_response('jams/jam.html',
                              {'jam': jam, 'hours': hours, 'minutes': minutes},
                              context_instance=RequestContext(request))
