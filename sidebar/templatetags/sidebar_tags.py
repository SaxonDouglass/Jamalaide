import datetime

from django import template
from django.shortcuts import get_list_or_404, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from jams.models import Jam

register = template.Library()

@register.inclusion_tag('sidebar.html')
def sidebar():
    nextJam = Jam.objects.filter(end__gt=datetime.datetime.now()).order_by('end')
    prevJam = Jam.objects.filter(end__lt=datetime.datetime.now()).order_by('-end')
    
    if nextJam:
        nextJam = nextJam[0]
    if prevJam:
        prevJam = prevJam[0]
    
    return { 'next': nextJam, 'prev': prevJam } 
    
