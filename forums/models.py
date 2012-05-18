from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Thread(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    first = models.ForeignKey('Post', related_name='+')
    last = models.ForeignKey('Post', related_name='+')
    updated = models.DateTimeField()
    
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

class LastRead(models.Model):
    user = models.ForeignKey(User)
    thread = models.ForeignKey(Thread)
    post = models.ForeignKey(Post, related_name='+')

def update_thread(sender, instance, created, **kwargs):
    if created:
        thread = instance.thread
        thread.updated = instance.posted
        thread.last = instance
        thread.save()

post_save.connect(update_thread, sender=Post)
