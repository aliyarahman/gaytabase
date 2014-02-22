# Import resources
import urlparse
from django.shortcuts import render, get_object_or_404
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
def SDView(request, SD_id):
	senatedistrict = get_object_or_404(SenateDistrict, pk=SD_id)
	return render(request, "SD.html", {'senatedistrict': senatedistrict })

@login_required
def HDView(request, HD_id):
	housedistrict = get_object_or_404(HouseDistrict, pk=HD_id)
	return render(request, "HD.html", {'housedistrict': housedistrict })

@login_required
def regionView(request, region_id):
	region = get_object_or_404(Region, pk=region_id)
	counties = County.objects.filter(region = region)
	senatedistricts = SenateDistrict.objects.filter(region = region)
	housedistricts = HouseDistrict.objects.filter(region = region)
	return render(request, "region.html", {'region':region, 'counties':counties, 'senatedistricts':senatedistricts, 'housedistricts':housedistricts})

@login_required
def countyView(request, county_id):
	county = get_object_or_404(County, pk=county_id)
	lowername = county.name.lower().replace(" ","")
	return render(request, "county.html", {'county': county, 'lowername':lowername})

@login_required
def cityView(request, city_id):
	city = get_object_or_404(City, pk=city_id)
	return render(request, "city.html", {'city': city })

@login_required
def SenatorView(request, Senator_id):
	senator = get_object_or_404(Senator, pk=Senator_id)
	return render(request, "Senator.html", {'senator': senator })
	
@login_required
def RepresentativeView(request, Representative_id):
	representative = get_object_or_404(Representative, pk=Representative_id)
	return render(request, "Representative.html", {'representative': representative })

@login_required
def businessView(request, business_id):
	business = get_object_or_404(Business, pk=business_id)	
	return render(request, "business.html", {'business': business })

@login_required
def organizationView(request, organization_id):
	organization = get_object_or_404(Organization, pk=organization_id)
	return render(request, "organization.html" , {'organization': organization })

@login_required
def leaderView(request, leader_id):
	leader = get_object_or_404(Leader, pk=leader_id)
	return render(request, "leader.html", {'leader': leader })
