from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bookmark(models.Model):
    """Describes a bookmark"""
    #user
   # owner = models.ForeignKey(User)
    #defines a readable nickname for a bookmark
    nickname = models.CharField(max_length=30)
    #bookmark url
    url = models.URLField()
    #a little description abou some bookmark
    description = models.TextField(max_length=1000)
    #date created
    date_created = models.DateTimeField(auto_now_add=True)