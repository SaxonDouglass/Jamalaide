from django.db import models
from django.contrib.auth.models import User

class Thread(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.title

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User)
    posted = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    thread = models.ForeignKey(Thread)
    message = models.TextField()
    
    def __unicode__(self):
        return self.thread.title + " - " + `self.id`
