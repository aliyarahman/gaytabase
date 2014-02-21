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
	senatedistrict = SenateDistrict.objects.get(number=1)
	legislator = Senator.objects.get(lastname = "Hite")
	return render(request, "SD.html", {'senatedistrict': senatedistrict, 'legislator': legislator })

def HDView(request):
	housedistrict = HouseDistrict.objects.get(number=81)
	legislator = Representative.objects.get(lastname = "Wachtmann")
	return render(request, "HD.html", {'housedistrict': housedistrict, 'legislator': legislator })

def regionView(request):
	region = Region.objects.get(name="Northwest")
	return render(request, "region.html", {'region':region})

def countyView(request):
	county = County.objects.get(name="Adams")
	return render(request, "county.html", {'county': county})

def cityView(request):
	city = City.objects.get(name = "Ada")
	return render(request, "city.html", {'city': city })

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
