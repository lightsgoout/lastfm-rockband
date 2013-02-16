from django.conf.urls import patterns, url
from django.views.generic.simple import direct_to_template
from recommend.views import view_recommends

urlpatterns = patterns('',
   url(r'^$',
       direct_to_template,
       {
           'template': 'landing.html'
       },
       name='landing'),
   url(r'^recommend/(?P<lastfm_username>[_\.a-zA-Z0-9-]+)/$',
       view_recommends,
       name='recommend'),
)
