from django.conf import settings
from django.db.models import Q
from django.shortcuts import render
from django.template import RequestContext
import lastfmapi
from recommend.models import Song


def view_recommends(request, lastfm_username):
    try:
        # todo: store in memcache
        api = lastfmapi.LastFmApi(settings.LASTFM_API_KEY)
        json = api.user_getTopArtists(
            user=lastfm_username,
            limit=100
        )

        q = Q()
        for json_artist in json['topartists']['artist']:
            q |= Q(artist__name__iexact=json_artist['name'])

        hits = Song.objects.filter(q)

        return render(request, 'recommend.html', {
            'hits': hits,
            'lastfm_username': lastfm_username,
        }, context_instance=RequestContext(request))

    except lastfmapi.LastFmApiException, e:
        return render(request, 'error.html', {
            'error': e
        })
