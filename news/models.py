from django.db import models
from datetime import datetime

class NewsItem(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(blank=True)
    details = models.TextField()
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.date = datetime.now()
        super(NewsItem, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.title
