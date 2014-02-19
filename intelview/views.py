# Import resources
from django.shortcuts import render
from intelview.models import User, Region, County, City, SenateDistrict, HouseDistrict, Senator, Representative, Business, Organization, Leader

# Landing page (see this after login)
def index(request):
	return render(request, 'index.html')

def places(request):
	return render(request, "places-menu.html")

#	cities = City.query.all()
#	counties = County.query.all()
#	senatedistricts = SenateDistrict.query.all()
#	housedistricts = HouseDistrict.query.all()
	# should include, cities = cities, counties=counties, senatedistricts=senatedistricts, housedistricts = housedistricts)
'''
def SD(shortcode):
	senatedistrict = SenateDistrict.query.filter_by(number=shortcode).first()
	legislator = Senator.query.filter_by(id = senatedistrict.representedBy).first()
	return render(request, 'SD.html', senatedistrict = senatedistrict, legislator = legislator)

def HD(shortcode):
	housedistrict = HouseDistrict.query.filter_by(shortcode=shortcode).first()
	legislator = Representative.query.filter_by(id = housedistrict.representedBy).first()
	return render(request, 'HD.html', housedistrict = housedistrict, legislator = legislator)
	
def city(name):
	city = City.query.filter_by(name=name).first()
	return render(request, 'city.html', city=city)

def county(name):
	county = County.query.filter_by(name=name).first()
	return render(request, 'county.html', county=county)
'''
def legislators(request):
	senators = Senator.objects.all()
	representatives = Representative.objects.all()
	return render(request, "legislators-menu.html", senators = senators, representatives = representatives)
	# should include, senators = senators, representatives=representatives)
'''
def Sen(id):
	senator = Senator.query.filter_by(id=id).first()
	return render(request, 'Senator.html', senator = senator)

def Rep(id):
	representative = Representative.query.filter_by(id=id).first()
	hd = HouseDistrict.query.filter_by(id = representative.id)
	return render(request, 'Representative.html', representative = representative, hd = hd)
'''
def businesses(request):
	return render(request, "businesses-menu.html")
'''
def business(name):
#	business = Business.query.filter_by(name=name).first()
	return render(request, 'business.html')
	# should include, business=business)
'''
def leaders(request):
	return render(request, "leaders-menu.html")
'''
def leader(id):
	leader = Leader.query.filter_by(id=id).first()
	return render(request, 'leader.html', leader=leader)
'''
def groups(request):
	return render(request, "groups-menu.html")

'''def group(name):
	group = Group.query.filter_by(name=name).first()
	return render(request, 'group.html', group=group)
'''
def help(request):
	return render(request, "help.html")

def forgot(request):
	return render(request, "forgot.html")
'''
def logout():
	logout_user()
	return redirect(url_for('index'))
	'''
