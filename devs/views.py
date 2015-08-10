from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from accounts.models import Profile, Team
from jams.models import Game

def devs(request):
    users = Profile.objects.all()
    teams = Team.objects.all()
    return render_to_response('devs/index.html',{ 'users': users, 'teams': teams },
                              context_instance=RequestContext(request))

def profile(request, slug):
    teams = Team.objects.filter(slug=slug)
    if teams:
        team = teams[0]
        games = Game.objects.filter(team=team)
        return render_to_response('devs/team.html',{ 'team': team, 'games': games },
                                  context_instance=RequestContext(request))
    else:
        profile = get_object_or_404(Profile, slug=slug)
        games = Game.objects.filter(creators=profile.user)
        return render_to_response('devs/user.html',{ 'profile': profile, 'games': games },
                                  context_instance=RequestContext(request))
