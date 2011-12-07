# Create your views here.

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.core.mail import send_mail

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
            return HttpResponseRedirect('/jams/ggj-2012/registered')
    else:
        form = RegistrationForm()
    
    c = { 'form':form }
    c.update(csrf(request))
    return render_to_response('jams/index.html', c)
