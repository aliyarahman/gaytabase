# Import resources
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from intelview.models import User, Region, County, City, SenateDistrict, HouseDistrict, Senator, Representative, Business, Organization, Leader

# Landing page (see this after login)
def index(request):
	return render(request, 'index.html')

#Menu pages
def places(request):
	senatedistricts = SenateDistrict.objects.all()
	housedistricts = HouseDistrict.objects.all()
	regions = Region.objects.all()
	counties = County.objects.all()
	cities = City.objects.all()
	return render(request, 'places-menu.html', {'senatedistricts':senatedistricts, 'housedistricts':housedistricts, 'regions':regions, 'counties':counties, 'cities':cities})

def legislators(request):
	Senators = Senator.objects.all()
	Representatives = Representative.objects.all()
	return render(request, "legislators-menu.html", {'Senators': Senators, 'Representatives':Representatives})

def leaders(request):
	leaders = Leader.objects.all()
	return render(request, "leaders-menu.html", {'leaders': leaders})

def businesses(request):
	businesses = Business.objects.all()
	return render(request, "businesses-menu.html", {'businesses': businesses})

def organizations(request):
	organizations = Organization.objects.all()
	return render(request, "organizations-menu.html", {'organizations': organizations})

#Banner pages
def help(request):
	return render(request, "help.html")

#Individual place pages
def SDView(request):
	return render(request, "SD.html")

def HDView(request):
	return render(request, "HD.html")

def regionView(request):
	return render(request, "region.html")

def countyView(request):
	county = County.objects.get(name="Adams")
	return render(request, "county.html", {'county': county})

def cityView(request):
	return render(request, "city.html")

def SenatorView(request):
	return render(request, "Senator.html")
	
def RepresentativeView(request):
	return render(request, "Representative.html")
	
def businessView(request):
	return render(request, "business.html")
	
def organizationView(request):
	return render(request, "organization.html")
	
def leaderView(request):
	return render(request, "leader.html")
