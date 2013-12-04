from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):    
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    brief = models.TextField(blank=True)
    def __unicode__(self):
        return self.user.get_full_name()

# Signal handlers
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def user_post_save_callback(sender, **kwargs):
    created = kwargs['created']
    instance = kwargs['instance']
    if created:
        profile = Profile();
        profile.user = instance
        profile.save()
