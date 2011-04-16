from django.conf.urls.defaults import *

urlpatterns = patterns('core.views',
    url(r'^$', 'talks', name='talks'),
    url(r'^(\d+)$', 'talk_details', name='talk_details'),
    url(r'^([-\w]+)/$','speaker',name='speaker'),
)