from django.db import models

class MailAccount(models.Model):
    priority = models.IntegerField()
    host = models.CharField(max_length=30)
    port = models.PositiveIntegerField()
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
