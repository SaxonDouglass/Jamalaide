from django.db import models

class NewsItem(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()#auto_now_add=True)
    details = models.TextField()
    
    def __unicode__(self):
        return self.title
