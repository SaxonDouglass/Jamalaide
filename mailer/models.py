from django.db import models

class Mail(models.Model):
    subject = models.CharField(max_length=69)
    body = models.TextField()
    recipients = models.ManyToManyField(User)
    
    SAVED = "SA"
    SENT = "SE"
    ERROR = "ER"
    STATES = (
        (SAVED, 'Saved'),
        (SENT, 'Sent'),
        (ERROR, 'Error'),
    )
    state = models.CharField(max_length=2,
                             choices=STATES,
                             default=SAVED)

class MailForm(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ('jam',)
