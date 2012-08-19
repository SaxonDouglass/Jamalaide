import datetime
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.core.files.base import ContentFile
from django.template.defaultfilters import slugify
from django.core.context_processors import csrf

from PIL import Image, ImageOps
import StringIO
import re

class JamManager(models.Manager):
    def get_current(self):
        from django.core.exceptions import ObjectDoesNotExist
        try:
            current = Jam.objects.get(start__lt=datetime.datetime.now(), end__gt=datetime.datetime.now())
        except ObjectDoesNotExist:
            return None
        except Jam.MultipleObjectsReturned:
            return None
        return current

class Jam(models.Model):
    objects = JamManager()
    
    name = models.CharField(max_length=50)
    url = models.SlugField(max_length=30)
    start = models.DateTimeField()
    end = models.DateTimeField()
    venue = models.TextField()
    website = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=30)
    url = models.SlugField(max_length=30, editable=False)
    jam = models.ForeignKey(Jam)
    creators = models.ManyToManyField(User)
    description = models.TextField()
    image = models.ImageField(upload_to=
        lambda instance, filename: 'game/'+instance.url+'/image',
        blank=True)
    thumbnail = models.FileField(upload_to=
        lambda instance, filename: 'game/'+instance.url+'/thumbnail',
        blank=True, editable=False)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id :
            self.url = slugify(self.name)
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
            self.thumbnail.save(name=self.image.name, content=cf, save=False);
        super(Game, self).save(*args, **kwargs)

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ('jam',)

class GameResource(models.Model):
    name = models.CharField(max_length=20)
    game = models.ForeignKey(Game,related_name='resources')
    link = models.CharField(max_length=256,blank=True,null=True)
    file = models.FileField(upload_to=lambda instance, filename: 'game/'+instance.game.url+'/'+slugify(instance.name),blank=True,null=True)
    url = models.CharField(max_length=256,editable=False)
    
    def save(self):
        super(GameResource, self).save()
        if self.link:
            self.url = self.link
        elif self.file:
            self.url = self.file.url
        else:
            self.url = ''
        super(GameResource, self).save()

    def __unicode__(self):
        return self.game.name+' ('+self.name+')'

class GameResourceForm(forms.ModelForm):
    class Meta:
        model = GameResource
        exclude = ('game',)
