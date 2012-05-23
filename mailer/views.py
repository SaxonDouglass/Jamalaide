import logging

from django import forms
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.core.mail import EmailMessage
from accounts.models import UserProfile

def send_mail(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            message = EmailMessage(form.cleaned_data['subject'],
                                   form.cleaned_data['body'],
                                   'notifications@jamalaide.appspotmail.com',
                                   headers = {'Reply-To': 'contact@jamalaide.org.au'})
            message.to = ["contact@jamalaide.org.au"]
            message.bcc = [profile.user.email for profile in UserProfile.objects.filter(notify=True)]
            message.send()
            logging.info('Email "%s" sent to %s', form.cleaned_data['subject'], message.recipients())
            return render_to_response('mailer/sent_mail.html', { 'subject': form.cleaned_data['subject'] })
    else:
        form = EmailForm()
    
    c = {'form': form}
    c.update(csrf(request))
    
    return render_to_response('mailer/send_mail.html', c)

class EmailForm(forms.Form):
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea())
