from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'body_wise.views.home', name='home'),
    # url(r'^body_wise/', include('body_wise.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^records/', include('records.urls', namespace='records')),
    url(r'^charts/', include('charts.urls')),
    url(r'', include('website.urls'))
)
