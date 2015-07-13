from django import template

from jams.models import Jam

register = template.Library()

@register.inclusion_tag('jams/jam_summary.html')
def jam_summary(jam):
    return { 'jam': jam }

@register.inclusion_tag('jams/game_thumb.html')
def game_thumb(game):
    return { 'game': game }

@register.filter
def duration(timedelta):
    hours = timedelta.days*24 + timedelta.seconds/3600
    minutes = timedelta.seconds%3600/60
    if minutes > 0:
        return str(hours)+" hours and "+str(minutes)+" minutes"
    else:
        return str(hours)+" hours"
