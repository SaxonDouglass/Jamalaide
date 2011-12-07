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
    return render_to_response('jams/jam.html', {'jam': jam})

def games(request):
    pass

def game(request):
    pass

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['email']
            send_mail('Register: '+name, name+'\n'+address, 'registrations@jamalaide.appspotmail.com', ['contact@jamalaide.org.au']);
            return HttpResponseRedirect('/jams/2012/01/27/registered')
    else:
        form = RegistrationForm()
    
    c = { 'form':form }
    c.update(csrf(request))
    return render_to_response('jams/index.html', c)

