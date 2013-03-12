from django.conf.urls import patterns, url
from website import views

urlpatterns = patterns('',
    url(r'^$', views.HomePage.as_view()),
    url(r'^splash$', views.Splash.as_view())
)
