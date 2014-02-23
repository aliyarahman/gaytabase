#!/usr/bin/env python

#Note this script must be run after running on the database:
#(i) Drop database SQL
#(ii) Create database SQL
#(iii) python manage.py syncdb

#Note that syncdb ONLY adds new tables. Does not modify existing tables. SQLclear command isn't doing it either.

import os
from intelview.models import Region, County, City, Senator, Representative, HouseDistrict, SenateDistrict, Business, Leader
from django.contrib.auth.models import User
import csv


#Add an admin user, two staff users, and a volunteer user
aliya = User.objects.create_user("aliya@equalityohio.org", "aliya@equalityohio.org", "P@ssw0rd123")
aliya.first_name = "Aliya"
aliya.last_name = "Rahman"
aliya.save()

elyzabeth = User.objects.create_user("elyzabeth@equalityohio.org","elyzabeth@equalityohio.org", "P@ssw0rd123")
elyzabeth.first_name = "Elyzabeth"
elyzabeth.last_name ="Holford"
elyzabeth.save()

kim = User.objects.create_user("kim@equalityohio.org","kim@equalityohio.org", "P@ssw0rd123")
kim.first_name = "Kim"
kim.last_name ="Welter"
kim.save()

grant = User.objects.create_user("grant@equalityohio.org","grant@equalityohio.org", "P@ssw0rd123")
grant.first_name = "Grant"
grant.last_name ="Stancliff"
grant.save()

shawn = User.objects.create_user("shawn@equalityohio.org","shawn@equalityohio.org", "P@ssw0rd123")
shawn.first_name = "Shawn"
shawn.last_name ="Copeland"
shawn.save()

tami = User.objects.create_user("tami@equalityohio.org","tami@equalityohio.org", "P@ssw0rd123")
tami.first_name = "Tami"
tami.last_name ="Lunan"
tami.save()

nicole = User.objects.create_user("nicole@equalityohio.org","nicole@equalityohio.org", "P@ssw0rd123")
nicole.first_name = "Nicole"
nicole.last_name ="Thomas"
nicole.save()

rashida = User.objects.create_user("rashida@equalityohio.org","rashida@equalityohio.org", "P@ssw0rd123")
rashida.first_name = "Rashida"
rashida.last_name ="Davison"
rashida.save()

volunteer1 = User.objects.create_user("volunteer1@equalityohio.org", "volunteer1@equalityohio.org", "P@ssw0rd123")
first_name = "Volunteer"
last_name ="One"
volunteer1.save()


#Create regions
NW = Region.objects.create(name = "Northwest", shortcode = "NW")
NE = Region.objects.create(name = "Northeast", shortcode = "NE")
SW = Region.objects.create(name = "Southwest", shortcode = "SW")
SE = Region.objects.create(name = "Southeast", shortcode = "SE")
CENT = Region.objects.create(name = "Central", shortcode = "CENT")



#Create counties
countynames = ["Adams","Allen","Ashland","Ashtabula","Athens","Auglaize","Belmont","Brown","Butler","Carroll","Champaign","Clark","Clermont","Clinton","Columbiana","Coshocton","Crawford","Cuyahoga","Darke","Defiance","Delaware","Erie","Fairfield","Fayette","Franklin","Fulton","Gallia","Geauga","Greene","Guernsey","Hamilton","Hancock","Hardin","Harrison","Henry","Highland","Hocking","Holmes","Huron","Jackson","Jefferson","Knox","Lake","Lawrence","Licking","Logan","Lorain","Lucas","Madison","Mahoning","Marion","Medina","Meigs","Mercer","Miami","Monroe","Montgomery","Morgan","Morrow","Muskingum","Noble","Ottawa","Paulding","Perry","Pickaway","Pike","Portage","Preble","Putnam","Richland","Ross","Sandusky","Scioto","Seneca","Shelby","Stark","Summit","Trumbull","Tuscarawas","Union","Van Wert","Vinton","Warren","Washington","Wayne","Williams","Wood","Wyandot"]

NWcounties = ["Williams", "Fulton", "Lucas", "Defiance", "Henry", "Wood", "Ottawa", "Sandusky", "Erie", "Huron", "Seneca", "Paulding", "Putnam", "Hancock", "Allen", "Auglaize", "Mercer", "Van Wert"]
NEcounties = ["Lorain", "Medina", "Wayne", "Stark", "Summit", "Portage", "Cuyahoga", "Lake", "Geauga", "Ashtabula", "Mahoning", "Trumbull"]
SWcounties = ["Darke", "Shelby", "Logan", "Miami", "Champaign", "Clark", "Preble", "Montgomery", "Greene", "Butler", "Warren", "Clinton", "Hamilton", "Clermont", "Brown"]
SEcounties = []
CENTcounties = ["Hardin", "Wyandot", "Crawford", "Richland", "Ashland", "Marion", "Knox", "Morrow", "Union", "Delaware", "Licking", "Franklin", "Madison", "Pickaway", "Fairfield", "Fayette"]

for n in countynames:
	if n in NWcounties:
		countyregion = Region.objects.get(shortcode = "NW")
	elif n in NEcounties:
		countyregion = Region.objects.get(shortcode = "NE")
	elif n in SWcounties:
		countyregion = Region.objects.get(shortcode = "SW")
	elif n in CENTcounties:
		countyregion = Region.objects.get(shortcode = "CENT")
	else:
		countyregion = Region.objects.get(shortcode = "SE")
	county = County.objects.create(name = n, region = countyregion)


#Add cities
ifile = open('cities.csv', "rb")
reader = csv.reader(ifile)
for row in reader:
	c = City(name = row[0], population = row[1])
	countyname1 = row[2].split(";")[0].split(" ")[0]
	if countyname1=="VanWert":
		countyname1="Van Wert"
	c.county = County.objects.get(name=countyname1)
	c.region = c.county.region
	c.save()

#Add SDs
NEsds = [13,18,21,22,23,24,25,27,28,29,32,33]
NWsds = [1,2,11,12,14,26]
SEsds = [30,20]
SWsds = [4,5,6,7,8,9,10]
CENTsds = [3,15,16,17,19,31]
ifile = open('SD_data.csv', "rb")
reader = csv.reader(ifile)
for row in reader:
	if int(row[0])<10:
		sdshortcode = "SD0"+row[0]
	else:
		sdshortcode = "SD"+row[0]
	if int(row[0]) in NWsds:
		sdregion = Region.objects.get(shortcode="NW")
	elif int(row[0]) in NEsds:
		sdregion = Region.objects.get(shortcode="NE")
	elif int(row[0]) in SWsds:
		sdregion = Region.objects.get(shortcode="SW")
	elif int(row[0]) in SEsds:
		sdregion = Region.objects.get(shortcode="SE")
	else:
		sdregion = Region.objects.get(shortcode="CENT")
	sd = SenateDistrict(number = row[0], shortcode = sdshortcode, region = sdregion)	
	sd.save()



#Add HDs
ifile = open('HD_data.csv', "rb")
reader = csv.reader(ifile)
for row in reader:
	if int(row[0])<10:
		hdshortcode = "HD0"+row[0]
	else:
		hdshortcode = "HD"+row[0]
	sdnumber = int(row[1])
	sd = SenateDistrict.objects.get(number=sdnumber)
	hdregion = sd.region
	hd = HouseDistrict(number = row[0], shortcode = hdshortcode, region = hdregion)
	hd.nestedInSD = sd
	hd.save()


#Add Senators
ifile = open('senator_data.csv', "rb")
reader = csv.reader(ifile)
for row in reader:
	sdistrict = SenateDistrict.objects.get(number=int(row[13]))
	region = sdistrict.region
	if row[4]=="1":
		EHEAstance = "Yes"
	if row[5]=="1":
		EHEAstance = "No"
	if row[6] == "1":
		EHEAstance="Maybe"

	if row[11] =="1":
		upforelection = "Yes"
	else:
		upforelection = "No"	

	if row[7]=="X":
		target =1
	else:
		target=0

	s = Senator(firstname=row[0], lastname=row[1], district=sdistrict, code=row[1], region=region, party = row[2], officePhone=row[3], currentEHEAstance=EHEAstance, EHEAtarget = target, EHEA2009Vote = row[8], committees2014=row[9], otherNotes = row[10], upin2014=upforelection, termLimit = row[12])
	s.save()



#Add Representatives
ifile = open('representative_data.csv', "rb")
reader = csv.reader(ifile)
for row in reader:
	hdistrict = HouseDistrict.objects.get(number=int(row[14]))
	region = hdistrict.region
	if row[6]=="1":
		EHEAstance = "Yes"
	if row[7]=="1":
		EHEAstance = "No"
	if row[8] == "1":
		EHEAstance="Maybe"
	if row[9]=="X":
		target =1
	else:
		target=0
	if row[1]=="Adams":
		if row[0]=="John":
			repcode = "AdamsJ"
		else:
			repcode = "AdamsR"
	else:
		repcode = row[1]

	r = Representative(firstname = row[0], lastname = row[1], district = hdistrict, code=repcode, region=region, party = row[2], title = row[3], officePhone=row[4], otherPhone = row[5], currentEHEAstance=EHEAstance, EHEAtarget = target, EHEA2009Vote = row[10], committees2014=row[11], profession=row[12], otherNotes = row[13], upin2014="Yes")
	r.save()
