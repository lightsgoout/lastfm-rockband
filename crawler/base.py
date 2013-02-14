# -*- coding: utf-8 -*-

import urllib2
import json
from recommend.models import Artist, Song, Genre


class RockbandCrawler(object):

    def update_db(self):

        page = urllib2.urlopen(
            'http://www.rockband.com/services.php/music/all-songs.json'
        )
        my_json = json.loads(page.read())
        for song_dict in my_json:

            artist, created = Artist.objects.get_or_create(
                name=song_dict['artist']
            )
            if created:
                artist.name_tr = song_dict['artist_tr']
                artist.save()
                print u'New artist created: %s' % artist

            genre, created = Genre.objects.get_or_create(
                name=song_dict['genre_symbol']
            )
            if created:
                print u'New genre created: %s' % genre

            song, created = Song.objects.get_or_create(
                short_name=song_dict['shortname'],
                artist=artist,
                genre=genre,
                year_released=int(song_dict['year_released']),
                name=song_dict['name'],
                name_tr=song_dict['name_tr'],
            )
            if created:
                song.is_rb3_only = song_dict['is_rb3_only']
                song.rating = song_dict['rating']
                song.source = song_dict['source']
                song.save()
                print u'New song created: %s' % song
