import datetime
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.forms.models import inlineformset_factory

from jams.models import *

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

def games(request):
    games = Game.objects.all()
    return render_to_response('jams/games.html', {'games': games},
                              context_instance=RequestContext(request))

def game(request, jam_url, game_url):
    jam = get_object_or_404(Jam, url=jam_url)
    game = get_object_or_404(Game, url=game_url, jam=jam)
    resources = GameResource.objects.filter(game=game)
    return render_to_response('jams/game.html',
        {'game': game, 'resources': resources},
        context_instance=RequestContext(request))

def edit_game(request, jam_url, game_url=None):
    ResourceFormSet = inlineformset_factory(Game, GameResource, extra=4, max_num=4)
    
    jam = get_object_or_404(Jam, url=jam_url)
    if game_url:
        game = get_object_or_404(Game, url=game_url)
        if request.user not in game.creators.all():
            return HttpResponseRedirect('/jams/'+game.jam.url+"/"+game.url)
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
            return HttpResponseRedirect('/jams/'+game.jam.url+"/"+game.url)
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

def edit_res(request, jam_url, game_url, res_id=None):
    game = get_object_or_404(Game, url=game_url)
    if res_id:
        res = get_object_or_404(GameResource, pk=res_id)
    else:
        res = GameResource()

    if request.method == 'POST':
        form = GameResourceForm(request.POST, request.FILES, instance=res)
        if request.user in game.creators.all() and form.is_valid():
            res = form.save(commit = False)
            res.game = game
            res.save()
            return HttpResponseRedirect('/jams/'+game.jam.url+"/"+game.url)
    else:
        form = GameResourceForm(instance=res)
    
    c = {
        'form':form,
        'res':res,
    }
    c.update(csrf(request))
    return render_to_response('jams/edit_res.html', c,
        context_instance=RequestContext(request))

def rm_res(request, jam_url, game_url, res_id=None):
    res = get_object_or_404(GameResource, pk=res_id)
    if request.user in res.game.creators.all():
        res.delete()
    return HttpResponseRedirect('/jams/'+res.game.jam.url+"/"+res.game.url)
