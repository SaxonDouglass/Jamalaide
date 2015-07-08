import datetime
import os
import re
import StringIO
from PIL import Image, ImageOps

from django import forms
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.core.files.base import ContentFile
from django.template.defaultfilters import slugify
from django.core.context_processors import csrf

class Jam(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=30)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    opening_times = models.CharField(max_length=100)
    venue = models.TextField()
    website = models.URLField(blank=True) # ?
    brief = models.TextField(blank=True)

    @property
    def is_current(self):
        now = datetime.datetime.now()
        return self.start_time < now and self.end_time > now
    
    def __unicode__(self):
        return self.title

def game_image_path(instance, filename):
    return 'jams/'+instance.jam.slug+'/'+instance.slug+'/image'

def game_thumb_path(instance,filename):
    return 'jams/'+instance.jam.slug+'/'+instance.slug+'/thumbnail'
    
class Game(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, editable=False, unique=True)
    jam = models.ForeignKey(Jam)
    creators = models.ManyToManyField(settings.AUTH_USER_MODEL)
    brief = models.TextField()
    spotlighted = models.BooleanField(default=False)
    image = models.ImageField(upload_to=game_image_path,
        blank=True)
    thumbnail = models.ImageField(upload_to=game_thumb_path,
        blank=True, editable=False)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_obj = Game.objects.get(pk = self.pk)
            if self.image is not None and self.image.path != old_obj.image.path:
                try:
                    os.remove(old_obj.image.path)
                except:
                    pass
        else:
            self.slug = slugify(self.title)

        try:
            os.remove(self.thumbnail.path)
        except:
            pass
        super(Game, self).save(*args, **kwargs)
        if self.image:
            imgFile = Image.open(self.image.path)
            if imgFile.mode not in ('L', 'RGB'):
                imgFile = imgFile.convert('RGB')
            working = imgFile.copy()
            working.thumbnail((192,144), Image.ANTIALIAS)
            fp = StringIO.StringIO()
            working.save(fp, "JPEG", quality=95)
            cf = ContentFile(fp.getvalue())
            try:
                os.remove(self.thumbnail.path)
            except:
                pass
            self.thumbnail.save(name=self.image.name, content=cf, save=False);
        super(Game, self).save(*args, **kwargs)

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ('jam', 'spotlighted')

def resource_file_path(instance, filename):
    return 'jams/'+ instance.game.jam.slug+'/'+instance.game.slug+'/'+ instance.game.slug+'-'+slugify(instance.title)+re.search("\.[^.]*$", filename).group()

class GameResource(models.Model):
    title = models.CharField(max_length=20)
    game = models.ForeignKey(Game,related_name='resources')
    link = models.CharField(max_length=256,blank=True,null=True)
    file = models.FileField(upload_to=resource_file_path ,blank=True,null=True)
    url = models.CharField(max_length=256,editable=False)

    def save(self):
        if self.pk is not None:
            old = GameResource.objects.get(pk = self.pk)
            if self.file is not None and self.file.path != old.file.path:
                try:
                    os.remove(old.file.path)
                except:
                    pass
        super(GameResource, self).save()
        if self.file:
            self.url = self.file.url
        elif self.link:
            self.url = self.link
        else:
            self.url = ''
        super(GameResource, self).save()

    def __unicode__(self):
        return self.game.title+' ('+self.title+')'

class GameResourceForm(forms.ModelForm):
    class Meta:
        model = GameResource
        exclude = ('game',)

def team_image_path(instance, filename):
        return 'jams/teams/'+instance.slug+'/image'

class Team(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, editable=False, unique=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL)
    brief = models.TextField(blank=True)
    image = models.ImageField(upload_to=team_image_path, blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Team, self).save(*args, **kwargs)
