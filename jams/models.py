from django.db import models
from djangotoolbox.fields import ListField

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=80)
    photo = models.FileField(upload_to='uploads/person/photo', blank=True)
    def __unicode__(self):
        return self.first_name+' '+self.last_name

class Jam(models.Model):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=30)
    start = models.DateTimeField()
    end = models.DateTimeField()
    venue = models.CharField(max_length=200)
    website = models.URLField(blank=True)
    def __unicode__(self):
        return self.name
    def duration(self):
        return str((self.end - self.start).days * 24 +
                (self.end - self.start).seconds / (60 * 60)) + " hours"

class Game(models.Model):
    name = models.CharField(max_length=80)
    url = models.CharField(max_length=30,editable=False)
    jam = models.ForeignKey(Jam,editable=False)
    image = models.FileField(upload_to='uploads/game/image', blank=True)
    game = models.FileField(upload_to='uploads/game/game', blank=True)
    source = models.FileField(upload_to='uploads/game/source', blank=True)
    def __unicode__(self):
        return self.name

class Creator(models.Model):
    person = models.ForeignKey(Person)
    game = models.ForeignKey(Game)
    def __unicode__(self):
        return self.game.name + " - " + self.person.first_name + " " + \
                self.person.last_name
