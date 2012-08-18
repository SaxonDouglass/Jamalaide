from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.core.files.base import ContentFile

from PIL import Image, ImageOps
import StringIO
import re

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

class Game(models.Model):
    name = models.CharField(max_length=80)
    url = models.SlugField(max_length=30, editable=False)
    jam = models.ForeignKey(Jam)
    creators = models.ManyToManyField(User)
    image = models.ImageField(upload_to='uploads/game/image', blank=True)
    thumbnail = models.FileField(upload_to='uploads/game/thumb', blank=True, editable=False)
    game = models.FileField(upload_to='uploads/game/game', blank=True)
    source = models.FileField(upload_to='uploads/game/source', blank=True)
    def __unicode__(self):
        return self.name
    def save(self):
        url = '-'.join(self.name.split()).lower()
        self.url = re.sub(r'[^\w-]+','',url)
        if self.image:
            imgFile = Image.open(self.image.path)
            if imgFile.mode not in ('L', 'RGB'):
                imgFile = imgFile.convert('RGB')
            working = imgFile.copy()
            working.thumbnail([192,144], Image.ANTIALIAS)
            fp = StringIO.StringIO()
            working.save(fp, "JPEG", quality=95)
            cf = ContentFile(fp.getvalue())
            self.thumbnail.save(name=self.image.name, content=cf, save=False);
        super(Game, self).save()  

# def create_game(sender, instance, **kwargs):
#     url = '-'.join(instance.name.split()).lower()
#     instance.url = re.sub(r'[^\w-]+','',url)
#     if instance.image:
#         image = Image.open(instance.image)
#         if image.mode not in ('L', 'RGB'):
#             image = image.convert('RGB')
#         x = 192
#         y = 144
#         img_ratio = float(image.size[0]) / image.size[1]
#         resize_ratio = float(x) / y
#         if img_ratio > resize_ratio:
#             output_width = x * image.size[1] / y
#             output_height = image.size[1]
#             originX = image.size[0] / 2 - output_width / 2
#             originY = 0
#         else:
#             output_width = image.size[0]
#             output_height = y * image.size[0] / x
#             originX = 0
#             originY = image.size[1] / 2 - output_height / 2
#         cropBox = (originX, originY, originX + output_width, originY + output_height)
#         image = image.crop(cropBox)
#         image.thumbnail([x, y], Image.ANTIALIAS)
#         thumb_io = StringIO.StringIO()
#         image.save(thumb_io, format='JPEG')
#         thumb_file = InMemoryUploadedFile(thumb_io, None, instance.image.name+'.jpg', 'image/jpeg',
#                                           thumb_io.len, None)
#         instance.thumbnail.save(instance.image.name+'.jpg',thumb_file)

# pre_save.connect(create_game, sender=Game)
