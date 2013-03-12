from django.conf.urls import patterns, url
from charts import views

urlpatterns = patterns('',
    url(r'^$', views.Grapher.as_view(), name='index'),

)
