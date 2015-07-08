import datetime

from django import template
from django.shortcuts import get_list_or_404, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from jams.models import Jam

register = template.Library()

@register.inclusion_tag('sidebar.html', takes_context = True)
def sidebar(context):
    request = context['request']
    upcoming = Jam.objects.filter(end_time__gt=datetime.datetime.now()).order_by('end_time')
    recent = Jam.objects.filter(end_time__lt=datetime.datetime.now()).order_by('-end_time')[:1]

    nextJam = None
    if len(upcoming) > 0:
        nextJam = upcoming[0]
    
    return { 'user': request.user, 'upcoming': upcoming[1:], 'next': nextJam, 'recent': recent} 
    
