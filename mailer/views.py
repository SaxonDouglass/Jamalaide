from django import forms
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.core.mail import EmailMessage
from email.mime.text import MIMEText
from accounts.models import UserProfile
from mailer.models import MailAccount

def send_mail(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            message = MIMEText(form.cleaned_data['body'])
            message['Subject'] = form.cleaned_data['subject']
            message['From'] = 'Jamalaide <contact@jamalaide.org.au>'
            recipients = UserProfile.objects.filter(notify=True)
            for m in MailAccount.objects.order_by('priority'):
                smtp = smtplib.SMTP( m.host , m.port )
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login( m.user, m.password )
                refused = smtp.sendMail('contact@jamalaide.org.au', recipients, message.as_string())
                smtp.quit()
                if len(refused) == 0:
                    return render_to_response('mailer/sent_mail.html', { 'subject': message['subject'] })
            return render_to_response('mailer/error_mail.html', { 'subject': message['subject'] })
    else:
        form = EmailForm()
    
    c = {'form': form}
    c.update(csrf(request))
    
    return render_to_response('mailer/send_mail.html', c)

class EmailForm(forms.Form):
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea())
