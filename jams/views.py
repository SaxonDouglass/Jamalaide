# Create your views here.

from django.http import HttpResponse
from django.core.mail import send_mail

def register(request):
    address = 'finn.stokes@gmail.com'
    name = 'Finn Stokes'
    contact = 'contact@jamalaide.org.au'
    send_mail('Register: '+name, name+'\n'+address, address, [contact]);
    return HttpResponse('Registering')
