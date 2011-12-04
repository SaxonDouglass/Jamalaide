from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=80)
    photo = models.ImageField(upload_to='file/img/person')
    
    def __unicode__(self):
        return self.first_name+' '+self.last_name

class Jam(models.Model):
    name = models.CharField(max_length=30)
    start = models.DateTimeField()
    end = models.DateTimeField()
    venue = models.CharField(max_length=200)
    website = models.URLField()
    
    def __unicode__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=80)
    creators = models.ManyToManyField(Person)
    jam = models.ForeignKey(Jam)
    image = models.ImageField(upload_to='file/img/game')
    game = models.FileField(upload_to='file/bin/game')
    source = models.FileField(upload_to='file/bin/src')
    
    def __unicode__(self):
        return self.name

