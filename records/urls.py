from django.conf.urls import patterns, url
from records import views

urlpatterns = patterns('',
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^submit/$', views.Submit.as_view(), name='submit')
)
