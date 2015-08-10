import itertools
import re

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

#from jams.models import Team

def profile_image_path(instance, filename):
    return 'accounts/'+instance.user.username+'/'+instance.user.username+re.search("\.[^.]*$", filename).group()

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=30, blank=True, verbose_name="Display Name")
    slug = models.SlugField(max_length=30, editable=False, unique=True)
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

    def save(self, *args, **kwargs):
        if not self.slug:
            max_length = Profile._meta.get_field('slug').max_length
            self.slug = orig = slugify(self.user.username)[:max_length]

            for x in itertools.count(1):
                if not Team.objects.filter(slug=self.slug).exists() and not Profile.objects.filter(slug=self.slug).exists():
                    break

                # Truncate the original slug dynamically. Minus 1 for the hyphen.
                self.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)

        super(Profile, self).save(*args, **kwargs)

def team_image_path(instance, filename):
    return 'teams/'+instance.slug+'/'+instance.slug+re.search("\.[^.]*$", filename).group()

class Team(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, editable=False, unique=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="teams")
    brief = models.TextField(max_length=300, blank=True)
    extended = models.TextField(blank=True)
    image = models.ImageField(upload_to=team_image_path, blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            max_length = Team._meta.get_field('slug').max_length
            self.slug = orig = slugify(self.name)[:max_length]

            for x in itertools.count(1):
                if not Team.objects.filter(slug=self.slug).exists() and not Profile.objects.filter(slug=self.slug).exists():
                    break

                # Truncate the original slug dynamically. Minus 1 for the hyphen.
                self.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)

        super(Team, self).save(*args, **kwargs)

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
