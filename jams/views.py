import datetime
from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404

from jams.models import Jam

def future(request):
    jams = get_list_or_404(Jam, end__gt=datetime.datetime.now())
    return render_to_response('jams/index.html', {'jams': jams, 'title': "Upcoming Jams"})

def past(request):
    jams = get_list_or_404(Jam, end__lt=datetime.datetime.now())
    return render_to_response('jams/index.html', {'jams': jams, 'title': "Jams"})

def jam(request, jam_url):
    jam = get_object_or_404(Jam, url=jam_url)
    duration = jam.end-jam.start
    hours = duration.days*24 + duration.seconds/3600
    minutes = duration.seconds%3600/60
    return render_to_response('jams/jam.html', {'jam': jam, 'hours': hours, 'minutes': minutes})
