from django.conf.urls import patterns, url

from intelview import views

urlpatterns = patterns('',
	url('', views.index, name='index'),
	url('index', views.index, name='index'),
    url('help', views.help, name='help'),
    url('places', views.places, name='places'),
    url('legislators', views.legislators, name='legislators'),
    url('businesses', views.businesses, name='businesses'),
    url('groups', views.groups, name='groups'),
    url('help', views.help, name='help'),
    url('leaders', views.leaders, name='leaders')
)
