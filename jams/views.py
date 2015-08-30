import datetime
from django.shortcuts import redirect, render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.forms.models import inlineformset_factory
from django.contrib.auth.decorators import login_required

from jams.models import *

def upcoming(request):
    return redirect('jams.views.jams', permanent=True)

def jams(request):
    current = list(Jam.objects.filter(start_time__lt=datetime.datetime.now(), end_time__gt=datetime.datetime.now()).order_by('end_time'))
    upcoming = list(Jam.objects.filter(start_time__gt=datetime.datetime.now()).order_by('end_time'))
    recent = list(Jam.objects.filter(end_time__lt=datetime.datetime.now()).order_by('-end_time'))

    nextJam = None
    if len(upcoming) > 0:
        nextJam = upcoming[0]

    recent_games = [(jam, jam.game_set.order_by('?')[:3]) for jam in recent[:2]]

    return render_to_response('jams/index.html',
                              {'current': current, 'next': nextJam, 'upcoming': upcoming[1:], 'recent': recent_games},
                              context_instance=RequestContext(request))

def jam(request, jam_slug):
    jam = get_object_or_404(Jam, slug=jam_slug)
    games = jam.game_set.all().order_by('title')
    news = jam.article_set.all().order_by('-date')
    
    if jam.end_time > datetime.datetime.now():
        return render_to_response('jams/future-jam.html',
                                  {'jam': jam, 'games': games, 'news': news},
                                  context_instance=RequestContext(request))
    else:
        return render_to_response('jams/past-jam.html',
                                  {'jam': jam, 'games': games, 'news': news},
                                  context_instance=RequestContext(request))

def games(request):
    recent = Jam.objects.filter(end_time__lt=datetime.datetime.now()).exclude(game=None).order_by('-end_time')[:2]
    recent_games = [(jam, jam.game_set.order_by('title')) for jam in recent]
    spotlighted = Game.objects.filter(spotlighted=True).exclude(jam__in=recent).order_by('title')
    games = Game.objects.filter(spotlighted=False).exclude(jam__in=recent).order_by('title')
    return render_to_response('jams/games.html', {'recent': recent_games, 'spotlight': spotlighted, 'games': games},
                              context_instance=RequestContext(request))

def game(request, jam_slug, game_slug):
    jam = get_object_or_404(Jam, slug=jam_slug)
    game = get_object_or_404(Game, slug=game_slug, jam=jam)
    resources = GameResource.objects.filter(game=game)

    jam_games = Game.objects.filter(jam=jam).exclude(pk=game.pk).order_by('?')[:5]
    
    return render_to_response('jams/game.html',
        {'jam': jam, 'game': game, 'jam_games': jam_games, 'resources': resources},
        context_instance=RequestContext(request))

@login_required
def edit_game(request, jam_slug, game_slug=None):
    ResourceFormSet = inlineformset_factory(Game, GameResource, fields=("title", "link", "file"), extra=4, max_num=4)
    
    jam = get_object_or_404(Jam, slug=jam_slug)
    if game_slug:
        game = get_object_or_404(Game, slug=game_slug)
        if request.user not in game.creators.all():
            return HttpResponseRedirect('/jams/'+game.jam.slug+"/"+game.slug)
    else:
        game = Game()
    
    if request.method == 'POST':
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
