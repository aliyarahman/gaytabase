from django.conf.urls import patterns, url, include
from intelview import views


urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^login/$', 'django.contrib.auth.views.login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout'),
	url(r'^index/$', views.index, name='index'),
	url(r'^places/$', views.places, name='places'),
	url(r'^legislators/$', views.legislators, name='legislators'),
	url(r'^leaders/$', views.leaders, name='leaders'),
	url(r'^businesses/$', views.businesses, name='businesses'),
	url(r'^organizations/$', views.organizations, name='organizations'),
	url(r'^help/$', views.help, name='help'),
	url(r'^SDView/(?P<SD_id>\d+)/$', views.SDView, name='SDView'),
	url(r'^HDView/(?P<HD_id>\d+)/$', views.HDView, name='HDView'),
	url(r'^regionView/(?P<region_id>\d+)/$', views.regionView, name='regionView'),
	url(r'^countyView/(?P<county_id>\d+)/$', views.countyView, name='countyView'),
	url(r'^cityView/(?P<city_id>\d+)/$', views.cityView, name='cityView'),
	url(r'^SenatorView/(?P<Senator_id>\d+)/$', views.SenatorView, name='SenatorView'),
	url(r'^RepresentativeView/(?P<Representative_id>\d+)/$', views.RepresentativeView, name='RepresentativeView'),
	url(r'^businessView/(?P<business_id>\d+)/$', views.businessView, name='businessView'),
	url(r'^organizationView/(?P<organization_id>\d+)/$', views.organizationView, name='organizationView'),
	url(r'^leaderView/(?P<leader_id>\d+)/$', views.leaderView, name='leaderView'),
)
