from django.conf.urls.default import *

urlpatterns = patterns('subscription.views',
    url(r'^$', subscribe, name='subscribe'),
    url(r'^(\d+)/sucesso/$', 'sucess', name='sucess'),
)
