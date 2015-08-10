import datetime
import itertools
import os
import re
import StringIO
from PIL import Image, ImageOps

from django.contrib.auth.models import User

from django import forms
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.core.files.base import ContentFile
from django.template.defaultfilters import slugify
from django.core.context_processors import csrf

from accounts.models import Team

def map_path(instance, filename):
    return 'jams/'+instance.slug+'/'+instance.slug+'-map'+re.search("\.[^.]*$", filename).group()

def map_svg_path(instance, filename):
    return 'jams/'+instance.slug+'/'+instance.slug+'-map.svg'

def banner_path(instance, filename):
    return 'jams/'+instance.slug+'/'+instance.slug+'-banner'+re.search("\.[^.]*$", filename).group()

def banner_svg_path(instance, filename):
    return 'jams/'+instance.slug+'/'+instance.slug+'-banner.svg'

def logo_path(instance, filename):
    return 'jams/'+instance.slug+'/'+instance.slug+'-logo'+re.search("\.[^.]*$", filename).group()

def logo_svg_path(instance, filename):
    return 'jams/'+instance.slug+'/'+instance.slug+'-logo.svg'

class Jam(models.Model):
    class Meta:
        permissions = (
            ("can_post", "Can post jams"),
            ("official", "Can post official jams"),
        )

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=30, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    actual_duration = models.FloatField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True)
    opening_times = models.TextField(max_length=100)
    venue = models.TextField()
    official = models.BooleanField(default=True)
    website_title = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    registration_title = models.CharField(max_length=100, default="Register now!", blank=True)
    registration = models.URLField(blank=True)
    brief = models.TextField(blank=True)
    schedule = models.TextField(blank=True)
    theme = models.CharField(max_length=100, blank=True)
    map = models.ImageField(upload_to=map_path, blank=True)
    map_svg = models.FileField(upload_to=map_svg_path, blank=True)
    map_link = models.URLField(blank=True)
    banner = models.ImageField(upload_to=banner_path, blank=True)
    banner_svg = models.FileField(upload_to=banner_svg_path, blank=True)
    logo = models.ImageField(upload_to=logo_path, blank=True)
    logo_svg = models.FileField(upload_to=logo_svg_path, blank=True)
    
    @property
    def is_current(self):
        now = datetime.datetime.now()
        return self.start_time < now and self.end_time > now
    
    @property
    def is_active(self):
        now = datetime.datetime.now()
        return self.start_time < now and self.deadline > now

    @property
    def duration(self):
        if not self.actual_duration:
            return self.end_time-self.start_time
        else:
            return datetime.timedelta(hours=self.actual_duration)
    
    def save(self, *args, **kwargs):
        if not self.deadline:
            self.deadline = self.end_time + datetime.timedelta(days=1)
        super(Jam, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

def game_image_path(instance, filename):
    return 'jams/'+instance.jam.slug+'/'+instance.slug+'/'+instance.slug+re.search("\.[^.]*$", filename).group()

def game_display_path(instance, filename):
    return 'jams/'+instance.jam.slug+'/'+instance.slug+'/image.png'

def game_thumb_path(instance,filename):
    return 'jams/'+instance.jam.slug+'/'+instance.slug+'/thumbnail.png'
    
class Game(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, editable=False)
    jam = models.ForeignKey(Jam)
    team = models.ManyToManyField(Team, blank=True)
    creators = models.ManyToManyField(settings.AUTH_USER_MODEL)
    brief = models.TextField()
    spotlighted = models.BooleanField(default=False)
    image = models.ImageField(upload_to=game_image_path, blank=True)
    display_image = models.ImageField(upload_to=game_display_path, blank=True, editable=False)
    thumbnail = models.ImageField(upload_to=game_thumb_path, blank=True, editable=False)

    class Meta:
        unique_together = ("jam", "slug")
    
    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_obj = Game.objects.get(pk = self.pk)
            if old_obj.image and (not self.image or self.image.path != old_obj.image.path):
                try:
                    os.remove(old_obj.image.path)
                except:
                    pass
        if not self.slug:
            max_length = Game._meta.get_field('slug').max_length
            self.slug = orig = slugify(self.title)[:max_length]

            for x in itertools.count(1):
                if not Game.objects.filter(slug=self.slug, jam=self.jam).exists():
                    break

                # Truncate the original slug dynamically. Minus 1 for the hyphen.
                self.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)

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
            working.thumbnail((600,450), Image.ANTIALIAS)
            fp = StringIO.StringIO()
            working.save(fp, "PNG", quality=95)
            cf = ContentFile(fp.getvalue())
            try:
                os.remove(self.display_image.path)
            except:
                pass
            self.display_image.save(name=self.image.name, content=cf, save=False);
            working = imgFile.copy()
            working.thumbnail((192,144), Image.ANTIALIAS)
            fp = StringIO.StringIO()
            working.save(fp, "PNG", quality=95)
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
    link = models.CharField(max_length=256,blank=True)
    file = models.FileField(upload_to=resource_file_path ,blank=True,null=True)
    url = models.CharField(max_length=256,editable=False)

    def save(self):
        if self.pk is not None:
            old = GameResource.objects.get(pk = self.pk)
            if old.file and (not self.file or self.file.path != old.file.path):
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
