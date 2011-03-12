from django.conf.urls.defaults import *

urlpatterns = patterns('core.views',    
    url(r'^([-\w]+)/$','speaker',name='speaker'),
  )