from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    content = models.TextField()

    def __unicode__(self):
        return self.title
