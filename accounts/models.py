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

class CommitteeMember(models.Model):
    class Meta:
        ordering = ['-priority', 'title', 'member__first_name', 'member__last_name', 'member__username']

    title = models.CharField(max_length=30, blank=True)
    priority = models.IntegerField(default=0)
    member = models.ForeignKey(settings.AUTH_USER_MODEL)
    email = models.EmailField(blank=True, null=True)

    def __unicode__(self):
        name = self.member.get_full_name()
        if (not name):
            name = self.member.username
        if self.title:
            return name + " ("+ self.title + ")"
        else:
            return name
