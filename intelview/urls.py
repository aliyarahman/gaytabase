from django.conf.urls import patterns, url, include
from intelview import views


urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url('login', 'django.contrib.auth.views.login'),
	url('logout', 'django.contrib.auth.views.logout'),
	url('index', views.index, name='index'),
	url('places', views.places, name='places'),
	url('legislators', views.legislators, name='legislators'),
	url('leaders', views.leaders, name='leaders'),
	url('businesses', views.businesses, name='businesses'),
	url('organizations', views.organizations, name='organizations'),
	url('help', views.help, name='help'),
	url('SDView', views.SDView, name='SDView'),
	url('HDView', views.HDView, name='HDView'),
	url('regionView', views.regionView, name='regionView'),
	url('countyView', views.countyView, name='countyView'),
	url('cityView', views.cityView, name='cityView'),
	url('SenatorView', views.SenatorView, name='SenatorView'),
	url('RepresentativeView', views.RepresentativeView, name='RepresentativeView'),
	url('businessView', views.businessView, name='businessView'),
	url('organizationView', views.organizationView, name='organizationView'),
	url('leaderView', views.leaderView, name='leaderView'),
)
