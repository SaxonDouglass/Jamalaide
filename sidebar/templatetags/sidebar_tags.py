import datetime

from django import template
from django.shortcuts import get_list_or_404, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from jams.models import Jam

register = template.Library()

@register.inclusion_tag('sidebar.html', takes_context=True)
def sidebar(context):
    currentJam = Jam.objects.get_current()
    nextJam = Jam.objects.filter(end__gt=datetime.datetime.now()).order_by('end')
    prevJam = Jam.objects.filter(end__lt=datetime.datetime.now()).order_by('-end')
    
    if nextJam:
        nextJam = nextJam[0]
    if prevJam:
        prevJam = prevJam[0]
    
    return { 'current': currentJam, 'next': nextJam, 'prev': prevJam} 
    
