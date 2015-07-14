from datetime import datetime

from django.conf import settings
from django.db import models

from jams.models import Jam

def image_path(instance, filename):
    return 'blogs/'+str(instance.pk)+'/'+filename

class Article(models.Model):
    class Meta:
        permissions = (
            ("can_post", "Can post articles"),
            ("official", "Can post official articles"),
        )
    
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateField(default=datetime.now)
    content = models.TextField()
    official = models.BooleanField(default=True)
    jams = models.ManyToManyField(Jam, blank=True)
    header = models.ImageField(upload_to=image_path, blank=True)
    footer = models.ImageField(upload_to=image_path, blank=True)
    
    def __unicode__(self):
        return self.title
