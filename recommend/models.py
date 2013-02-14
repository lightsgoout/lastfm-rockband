# -*- coding: utf-8 -*-

from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255, unique=True)
    name_tr = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % self.name


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return u'%s' % self.name


class Song(models.Model):
    name = models.CharField(max_length=255)
    name_tr = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255, unique=True)
    artist = models.ForeignKey(Artist, related_name='songs')
    genre = models.ForeignKey(Genre, related_name='songs')
    year_released = models.PositiveSmallIntegerField()
    is_rb3_only = models.BooleanField(default=False)
    rating = models.PositiveSmallIntegerField(null=True)
    source = models.CharField(max_length=16, null=True)

    def __unicode__(self):
        return u'%s by %s (%s - %s)' % (
            self.name,
            self.artist,
            self.year_released,
            self.genre
        )
