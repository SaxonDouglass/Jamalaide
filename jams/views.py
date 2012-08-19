import datetime
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext

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
    games = get_list_or_404(Game, )
    return render_to_response('jams/games.html', {'games': games},
                              context_instance=RequestContext(request))

def game(request, jam_url, game_url):
    jam = get_object_or_404(Jam, url=jam_url)
    game = get_object_or_404(Game, url=game_url, jam=jam)
    resources = GameResource.objects.filter(game=game)
    return render_to_response('jams/game.html',
        {'game': game, 'resources': resources},
        context_instance=RequestContext(request))

def submit(request, jam_url):
    jam = get_object_or_404(Jam, url=jam_url)
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save()
            return HttpResponseRedirect('/jams/'+game.jam.url+"/"+game.url)
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
