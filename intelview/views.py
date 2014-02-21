# Import resources
import urlparse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from intelview.models import User, Region, County, City, SenateDistrict, HouseDistrict, Senator, Representative, Business, Organization, Leader

#Login page
def login(request):
	username =request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
		
#Logout page
def logout(request):
	logout(request)

# Main menu (see this after login)
@login_required
def index(request):
	return render(request, 'index.html')

#Menu pages
@login_required
def places(request):
	senatedistricts = SenateDistrict.objects.all()
	housedistricts = HouseDistrict.objects.all()
	regions = Region.objects.all()
	counties = County.objects.all()
	cities = City.objects.all()
	return render(request, 'places-menu.html', {'senatedistricts':senatedistricts, 'housedistricts':housedistricts, 'regions':regions, 'counties':counties, 'cities':cities})

@login_required
def legislators(request):
	Senators = Senator.objects.all()
	Representatives = Representative.objects.all()
	return render(request, "legislators-menu.html", {'Senators': Senators, 'Representatives':Representatives})

@login_required
def leaders(request):
	leaders = Leader.objects.all()
	return render(request, "leaders-menu.html", {'leaders': leaders})

@login_required
def businesses(request):
	businesses = Business.objects.all()
	return render(request, "businesses-menu.html", {'businesses': businesses})

@login_required
def organizations(request):
	organizations = Organization.objects.all()
	return render(request, "organizations-menu.html", {'organizations': organizations})


#Banner pages
def help(request):
	return render(request, "help.html")

#Individual place pages
@login_required
def SDView(request):
	senatedistrict = SenateDistrict.objects.get(number=1)
	legislator = Senator.objects.get(lastname = "Hite")
	return render(request, "SD.html", {'senatedistrict': senatedistrict, 'legislator': legislator })

@login_required
def HDView(request):
	housedistrict = HouseDistrict.objects.get(number=81)
	legislator = Representative.objects.get(lastname = "Wachtmann")
	return render(request, "HD.html", {'housedistrict': housedistrict, 'legislator': legislator })

@login_required
def regionView(request):
	region = Region.objects.get(name="Northwest")
	return render(request, "region.html", {'region':region})

@login_required
def countyView(request):
	county = County.objects.get(name="Adams")
	return render(request, "county.html", {'county': county})

@login_required
def cityView(request):
	city = City.objects.get(name = "Ada")
	return render(request, "city.html", {'city': city })

@login_required
def SenatorView(request):
	return render(request, "Senator.html")
	
@login_required
def RepresentativeView(request):
	return render(request, "Representative.html")

@login_required
def businessView(request):
	return render(request, "business.html")

@login_required
def organizationView(request):
	return render(request, "organization.html")

@login_required
def leaderView(request):
	return render(request, "leader.html")
