import re

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

def profile_image_path(instance, filename):
    return 'accounts/'+instance.user.username+'/'+instance.user.username+re.search("\.[^.]*$", filename).group()

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=30, blank=True, verbose_name="Display Name")
    image = models.ImageField(upload_to=profile_image_path, blank=True, verbose_name="Profile Image")
    show_email = models.BooleanField(default=False, help_text="Show email address on your public profile")
    brief = models.TextField(max_length=300, blank=True, verbose_name="Brief Description/Bio", help_text="(max length: 300 characters)")
    extended = models.TextField(blank=True, verbose_name="Extended Description/Bio")

    def __unicode__(self):
        return self.get_full_name()

    def get_full_name(self):
        if self.name:
            return self.name
        elif self.user.get_full_name():
            return self.user.get_full_name()
        else:
            return self.user.username

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

class CaptchaQuestion(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=30)

    def __unicode__(self):
        return self.question

class ContactLink(models.Model):
    class Meta:
        ordering = ['-priority', 'type']
    
    type = models.CharField(max_length=30, blank=True)
    priority = models.IntegerField(default=0)
    description = models.CharField(max_length=100)
    link = models.CharField(max_length=100)

    def __unicode__(self):
        return self.description
