from django.conf.urls import patterns, url

from intelview import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index')
)
