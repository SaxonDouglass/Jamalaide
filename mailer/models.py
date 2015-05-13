from django import forms
from django.conf import settings
from django.db import models

SAVED = "SA"
SENT = "SE"
ERROR = "ER"
STATES = (
    (SAVED, 'Saved'),
    (SENT, 'Sent'),
    (ERROR, 'Error'),
)

class Mail(models.Model):
    subject = models.CharField(max_length=69)
    body = models.TextField()
    recipients = models.ManyToManyField(settings.AUTH_USER_MODEL)
    state = models.CharField(max_length=2,
                             choices=STATES,
                             default=SAVED)

class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ('subject', 'body', 'recipients', 'state')
