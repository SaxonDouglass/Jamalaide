from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.core.mail import send_mail

from jams.models import *

from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404

from filetransfers.api import prepare_upload, serve_file

from PIL import Image, ImageOps

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

class GameForm(forms.ModelForm):
    creators = forms.ModelMultipleChoiceField(queryset=Person.objects.all())

    class Meta:
        model = Game

def submit(request, jam_url):
    jam = get_object_or_404(Jam, url=jam_url)
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            url = '-'.join(game.name.split()).lower()
            url = re.sub(r'[^\w-]+','',url)
            game.jam=jam
            game.url = url
            if 'image' in request.FILES:
                game.image = form.cleaned_data['image']
                image = Image.open(game.image)
                if image.mode not in ('L', 'RGB'):
                    image = image.convert('RGB')
                x = 192
                y = 144
                img_ratio = float(image.size[0]) / image.size[1]
                resize_ratio = float(x) / y
                if img_ratio > resize_ratio:
                    output_width = x * image_size[1] / y
                    output_height = image.size[1]
                    originX = image.size[0] / 2 - output_width / 2
                    originY = 0
                else:
                    output_width = image.size[0]
                    output_height = y * image_size[0] / x
                    originX = 0
                    originY = image.size[1] / 2 - output_height / 2
                cropBox = (originX, originY, originX + output_width, originY + output_height)
                image = image.crop(cropBox)
                image.thumbnail([x, y], Image.ANTIALIAS)
                game.thumbnail = image
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
    
    upload_url, upload_data = prepare_upload(request, '/jams/'+jam.url+'/submit')
    
    c = {
        'form':form,
        'jam':jam,
        'upload_url':upload_url,
        'upload_data':upload_data,
    }
    c.update(csrf(request))
    return render_to_response('jams/submit.html', c)

def download_image(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return serve_file(request, game.image)

def download_thumb(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return serve_file(request, game.thumbnail)

def download_source(request, pk):
    game = get_object_or_404(Game, pk=pk)
    pattern = re.compile('([.][^/]+)$')
    ext = pattern.search(game.source.name).group(0)
    return serve_file(request, game.source, save_as=game.url+"-src"+ext)

def download_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    pattern = re.compile('([.][^/]+)$')
    ext = pattern.search(game.game.name).group(0)
    return serve_file(request, game.game, save_as=game.url+"-game"+ext)
