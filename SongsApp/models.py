from django.db import models

class Song(models.Model):
    song_title = models.CharField(max_length=200)
    singer = models.CharField(max_length=200)
    release_date = models.DateField('release date')
