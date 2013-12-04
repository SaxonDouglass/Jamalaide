from datetime import datetime

from django.conf import settings
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateField(blank=True)
    content = models.TextField()
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.date = datetime.now()
        super(Article, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.title

class Image(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    image = models.ImageField(upload_to=
        lambda instance, filename: 'blogs/image/'+instance.owner.slug,
        blank=True)
