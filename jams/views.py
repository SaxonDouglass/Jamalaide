import datetime
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.forms.models import inlineformset_factory

from jams.models import *

def future(request):
    jams = Jam.objects.filter(end_time__gt=datetime.datetime.now()).order_by('end_time')
    return render_to_response('jams/index.html',
                              {'jams': jams, 'title': "Upcoming Jams"},
                              context_instance=RequestContext(request))

def past(request):
    jams = Jam.objects.filter(end_time__lt=datetime.datetime.now()).order_by('-end_time')
    return render_to_response('jams/index.html',
                              {'jams': jams, 'title': "Jams"},
                              context_instance=RequestContext(request))

def jam(request, jam_slug):
    jam = get_object_or_404(Jam, slug=jam_slug)
    duration = jam.end_time-jam.start_time
    hours = duration.days*24 + duration.seconds/3600
    minutes = duration.seconds%3600/60
    games = jam.game_set
    return render_to_response('jams/jam.html',
                              {'jam': jam, 'hours': hours, 'minutes': minutes, 'games': games},
                              context_instance=RequestContext(request))

def games(request):
    recent = Jam.objects.filter(end_time__lt=datetime.datetime.now()).exclude(game=None).order_by('-end_time')[:2]
    spotlighted = Game.objects.filter(spotlighted=True).exclude(jam__in=recent)
    games = Game.objects.filter(spotlighted=False).exclude(jam__in=recent)
    return render_to_response('jams/games.html', {'recent': recent, 'spotlight': spotlighted, 'games': games},
                              context_instance=RequestContext(request))

def game(request, jam_slug, game_slug):
    jam = get_object_or_404(Jam, slug=jam_slug)
    game = get_object_or_404(Game, slug=game_slug, jam=jam)
    resources = GameResource.objects.filter(game=game)
    return render_to_response('jams/game.html',
        {'game': game, 'resources': resources},
        context_instance=RequestContext(request))

def edit_game(request, jam_slug, game_slug=None):
    ResourceFormSet = inlineformset_factory(Game, GameResource, extra=4, max_num=4)
    
    jam = get_object_or_404(Jam, slug=jam_slug)
    if game_slug:
        game = get_object_or_404(Game, slug=game_slug)
        if request.user not in game.creators.all():
            return HttpResponseRedirect('/jams/'+game.jam.slug+"/"+game.slug)
    else:
        game = Game()
    
    if request.method == 'POST':
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login')
        form = GameForm(request.POST, request.FILES, instance=game)
        formset = ResourceFormSet(request.POST, request.FILES,
            instance=game)
        if form.is_valid() and formset.is_valid():
            game = form.save(commit = False)
            game.jam = jam
            game.save()
            game.creators.add(request.user)
            game.save()
            
            formset.save()
            return HttpResponseRedirect('/jams/'+game.jam.slug+"/"+game.slug)
    else:
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login')
        form = GameForm(instance=game)
        formset = ResourceFormSet(instance=game)
    
    c = {
        'form':form,
        'formset': formset,
        'jam':jam,
        'game': game,
    }
    c.update(csrf(request))
    return render_to_response('jams/edit_game.html', c,
        context_instance=RequestContext(request))
