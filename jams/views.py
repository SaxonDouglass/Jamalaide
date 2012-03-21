from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.core.mail import send_mail

from jams.models import Jam

from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404

def index(request):
    jams = get_list_or_404(Jam, )
    return render_to_response('jams/index.html', {'jams': jams})

def jam(request, jam_url):
    jam = get_object_or_404(Jam, url=jam_url)
    duration = jam.end-jam.start
    hours = duration.days*24 + duration.seconds/3600
    minutes = duration.seconds%3600/60
    return render_to_response('jams/jam.html', {'jam': jam, 'hours': hours, 'minutes': minutes})
