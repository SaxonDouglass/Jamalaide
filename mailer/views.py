from django import forms
from django.core.mail import EmailMessage
from accounts.models import UserProfile

def send_mail(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            message = EmailMessage(form.cleaned_data['subject'],
                                   form.cleaned_data['body'],
                                   'Jamalaide <contact@jamalaide.org.au>',
                                   bcc = UserProfile.mailing_list())
            message.send()
            return render_to_response('mailer/sent_mail.html')
    else:
        form = EmailForm()
    
    c = {'form': form}
    c.update(csrf(request))
    
    return render_to_response('mailer/send_mail.html', c)

class EmailForm(forms.Form):
    subject = forms.CharField()
    body = forms.TextField()
