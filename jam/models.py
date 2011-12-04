from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=80)
    authors = models.ManyToManyField(Person)
    contributors = models.ManyToManyField(Person)
    jam = models.ForeignKey(Jam)

