import datetime

from django import template
from django.shortcuts import get_list_or_404, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from jams.models import Jam

register = template.Library()

@register.inclusion_tag('sidebar.html', takes_context = True)
def sidebar(context):
    request = context['request']
    currentJam = Jam.objects.get_current()
    nextJam = Jam.objects.filter(end_time__gt=datetime.datetime.now()).order_by('end_time')
    prevJam = Jam.objects.filter(end_time__lt=datetime.datetime.now()).order_by('-end_time')
    
    if nextJam:
        nextJam = nextJam[0]
    if prevJam:
        prevJam = prevJam[0]
    
    return { 'user': request.user, 'current': currentJam, 'next': nextJam, 'prev': prevJam} 
    
