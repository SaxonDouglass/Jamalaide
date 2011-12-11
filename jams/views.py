from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.core.mail import send_mail

from jams.models import *

from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404

import re

def index(request):
    jams = get_list_or_404(Jam, )
    return render_to_response('jams/index.html', {'jams': jams})

def jam(request, jam_url):
    jam = get_object_or_404(Jam, url=jam_url)
    return render_to_response('jams/jam.html', {'jam': jam})

def games(request):
    games = get_list_or_404(Game, )
    return render_to_response('jams/games.html', {'games': games})

def game(request, jam_url, game_url):
    jam = get_object_or_404(Jam, url=jam_url)
    game = get_object_or_404(Game, url=game_url, jam=jam)
    creators = get_list_or_404(Creator, game=game)
    return render_to_response('jams/game.html', {'game': game, 'creators': creators})

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

class GameForm(forms.Form):
    name = forms.CharField(max_length=80)
    creators = forms.ModelMultipleChoiceField(queryset=Person.objects.all())
    image = forms.FileField(required=False)
    game = forms.FileField(required=False)
    source = forms.FileField(required=False)

def submit(request, jam_url):
    jam = get_object_or_404(Jam, url=jam_url)
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            url = '-'.join(name.split()).lower()
            url = re.sub(r'[^\w-]+','',url)
            game = Game(
                name=name,
                url=url,
                jam=jam,
            )
            if 'image' in request.FILES:
                game.image = form.cleaned_data['image']
            if 'game' in request.FILES:
                game.game = form.cleaned_data['game']
            if 'source' in request.FILES:
                game.source = form.cleaned_data['source']
            game.save()
            for person in form.cleaned_data['creators']:
                creator = Creator(
                    person=person,
                    game=game,
                )
                creator.save()
            return HttpResponseRedirect('/jams/'+jam.url+"/"+game.url)
    else:
        form = GameForm()
    
    c = {
        'form':form,
        'jam':jam,
    }
    c.update(csrf(request))
    return render_to_response('jams/submit.html', c)
