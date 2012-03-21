from django.db import models

class Jam(models.Model):
    name = models.CharField(max_length=50)
    url = models.SlugField(max_length=30)
    start = models.DateTimeField()
    end = models.DateTimeField()
    venue = models.TextField()
    website = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name
