from django.conf.urls.defaults import *
from django.conf import settings
from core.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', homepage),
    (r'inscricao/', include('subscription.urls', namespace='subscription')),
    (r'^palestrante/', include('core.urls', namespace='core')),
    (r'^palestras/', include('core.urls', namespace='core')),
    # Example:
    # (r'^eventex/', include('eventex.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$',
    'django.views.static.serve',
    { 'document_root': settings.MEDIA_ROOT }),
)
