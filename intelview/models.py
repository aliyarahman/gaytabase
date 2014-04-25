from django.db import models
from django.contrib.auth.models import User

''' Django has custom User object, and its fields are:
class User(models.Model):
	username
	password
	email
	first_name
	last_name'''

class Region(models.Model):
	name = models.CharField(max_length=15, unique = True)
	shortcode = models.CharField(max_length=4)
	otherNotes = models.CharField(max_length=400, default = "")

	def __unicode__(self):
		return self.name


class County(models.Model):
	name = models.CharField(max_length=30, unique = True)
	region = models.ForeignKey(Region)
	otherNotes = models.CharField(max_length=400, default = "")
	
	def __unicode__(self):
		return self.name


class City(models.Model):
	name = models.CharField(max_length=30, unique = True)
	county = models.ForeignKey(County)
	region = models.ForeignKey(Region)
	population = models.IntegerField(max_length=7, default = 0)
	localLegislation = models.CharField(max_length=400, default = "N/A")
	otherNotes = models.CharField(max_length=400, default = "")

	def __unicode__(self):
		return self.name

class SenateDistrict(models.Model):
	number = models.IntegerField()
	shortcode = models.CharField(max_length=4)
	region = models.ForeignKey(Region)
	DPI = models.CharField(max_length=20, default = [])
	cities = models.ManyToManyField(City, default = [])
	counties = models.ManyToManyField(County, default = [])
	
	def __unicode__(self):
		return self.shortcode

class HouseDistrict(models.Model):
	number = models.IntegerField()
	shortcode = models.CharField(max_length=4)
	region = models.ForeignKey(Region)
	nestedInSD = models.ForeignKey(SenateDistrict)
	DPI = models.CharField(max_length=20, default = [])
	cities = models.ManyToManyField(City, default =[])
	counties = models.ManyToManyField(County, default = [])

	def __unicode__(self):
		return self.shortcode


class Senator(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	code = models.CharField(max_length=20)
	district = models.ForeignKey(SenateDistrict)
	region = models.ForeignKey(Region)
	party = models.CharField(max_length=1)
	EHEAtarget = models.IntegerField(max_length=1)
	currentEHEAstance = models.CharField(max_length=5)
	EHEA2009Vote = models.CharField(max_length=8)
	lobbyDay2013Intel = models.CharField(max_length=400)
	committees2014 = models.CharField(max_length=400)
	upin2014  = models.CharField(max_length=4, default = "Yes")
	termLimit = models.IntegerField(max_length=4, default = 0)
	previousTerms = models.CharField(max_length=400, default="")
	livesInCity = models.CharField(max_length=400, default="")
	faithAffiliation = models.CharField(max_length=400, default="")
	profession = models.CharField(max_length=400, default = "")
	family = models.CharField(max_length=400, default = "")
	college = models.CharField(max_length=400, default = "")
	communityActivities  = models.CharField(max_length=400, default = "")
	officePhone = models.CharField(max_length=14)
	otherPhone = models.CharField(max_length=14, default = "")
	officeAddress = models.CharField(max_length=400, default = "")
	homeAddress = models.CharField(max_length=400, default = "")
	officeEmail = models.CharField(max_length=400, default = "")
	personalEmail = models.CharField(max_length=400, default = "")
	otherNotes = models.CharField(max_length=400)

	def __unicode__(self):
		return self.lastname


class Representative(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	title = models.CharField(max_length=45, default="")
	code = models.CharField(max_length=20)
	district = models.ForeignKey(HouseDistrict)
	region = models.ForeignKey(Region)
	party = models.CharField(max_length=1)
	EHEAtarget = models.IntegerField(max_length=1)
	currentEHEAstance = models.CharField(max_length=5)
	EHEA2009Vote = models.CharField(max_length=8)
	lobbyDay2013Intel = models.CharField(max_length=400, default = "")
	committees2014 = models.CharField(max_length=400, default = "")
	upin2014  = models.CharField(max_length=4, default = "Yes")
	termLimit = models.IntegerField(max_length=4, default=0)
	previousTerms = models.CharField(max_length=400, default = "")
	faithAffiliation = models.CharField(max_length=400, default = "")
	profession = models.CharField(max_length=400, default = "")
	family = models.CharField(max_length=400, default = "")
	college = models.CharField(max_length=400, default = "")
	communityActivities = models.CharField(max_length=400, default = "")
	officePhone = models.CharField(max_length=14, default = "")
	otherPhone = models.CharField(max_length=14, default = "")
	officeAddress = models.CharField(max_length=400, default = "")
	homeAddress = models.CharField(max_length=400, default = "")
	officeEmail = models.CharField(max_length=400, default = "")
	personalEmail = models.CharField(max_length=400, default = "")
	otherNotes = models.CharField(max_length=400, default = "")

	def __unicode__(self):
		return self.lastname


class Business(models.Model):
	name = models.CharField(max_length=45, unique = True)
	regions = models.ManyToManyField(Region, default = [])
	cities = models.ManyToManyField(City, default = [])
	counties = models.ManyToManyField(County, default = [])
	inSDs = models.ManyToManyField(SenateDistrict)
	inHDs = models.ManyToManyField(HouseDistrict)
	description = models.CharField(max_length=400, default = "")
	LGBTowned = models.IntegerField(max_length=1, default = 2)
	#LGBTowned codes for businesses: #0 = No, #1 = Yes, #2 = Unknown
	pointOfContact = models.CharField(max_length=400, default="")
	titleOfContact = models.CharField(max_length=100, default="")
	signedENDA = models.IntegerField(max_length=1, default = 0)
	jobsOhio =models.IntegerField(max_length=1, default = 2)
	smallBusiness =models.IntegerField(max_length=1, default = 2)	
	corporate =models.IntegerField(max_length=1, default = 2)	
	hasSOnondiscrim = models.IntegerField(max_length=1, default = 2)
	hasGInondiscrim = models.IntegerField(max_length=1, default = 2)
	hasSSDPBenefits = models.IntegerField(max_length=1, default = 2)
	HRCscore = models.IntegerField(max_length=3, default = 0)
	otherNotes = models.CharField(max_length=400, default = "")

	def __unicode__(self):
		return self.name


class Leader(models.Model):
	firstname = models.CharField(max_length=400)
	lastname = models.CharField(max_length=400)
	title= models.CharField(max_length=400, default ="")
	email = models.CharField(max_length=45, default ="")
	phone = models.CharField(max_length=400, default ="")
	address = models.CharField(max_length=400, default ="")
	city = models.ForeignKey(City, default ="")
	county = models.ForeignKey(County, default ="")
	zip = models.CharField(max_length=12, default = "")
	region = models.ForeignKey(Region, default ="")
	SDs = models.ManyToManyField(SenateDistrict, default = [])
	HDs = models.ManyToManyField(HouseDistrict, default = [])
	communityleader = models.IntegerField(max_length=1)
	faithleader = models.IntegerField(max_length=1)
	volunteerleader = models.IntegerField(max_length=1)
	businessleader = models.IntegerField(max_length=1)
	denomination = models.CharField(max_length=400, default ="")
	organizations = models.CharField(max_length=400, default = "")
	otherNotes = models.CharField(max_length=400, default ="")
	signedENDA = models.IntegerField(max_length=1)
	
	def __unicode__(self):
		return self.firstname


class Organization(models.Model):
	name = models.CharField(max_length=45, unique = True)
	LocalStateNationalAffinity = models.CharField(max_length=4, default = "")
	description = models.CharField(max_length=400, default = "")
	progressiveOrg = models.IntegerField(max_length=1, default =0)
	affinityGroup = models.IntegerField(max_length=1, default =0)
	nonprofitOrg = models.IntegerField(max_length=1, default =0)
	conservativeOrg = models.IntegerField(max_length=1, default =0)			
	primaryContact = models.ManyToManyField(Leader, default = [])
	regions = models.ManyToManyField(Region, default = [])
	counties = models.ManyToManyField(County, default = [])
	cities = models.ManyToManyField(City, default = [])
	inSDs = models.ManyToManyField(SenateDistrict, default = [])
	inHDs = models.ManyToManyField(HouseDistrict, default = [])
	otherNotes = models.CharField(max_length=400, default = "")

	def __unicode__(self):
		return self.name


class Donation(models.Model):
	amount = models.DecimalField(max_digits = 20, decimal_places =2, default="0.00")
	business = models.ForeignKey(City, default =[])
	individual = models.ForeignKey(Leader, default =[])
	toSenator = models.ForeignKey(Senator, default =[])
	toRep = models.ForeignKey(Representative, default =[])
	year = models.IntegerField(max_length=4, default = 2010)
	notes = models.CharField(max_length = 400, default = "")

	def __unicode__(self):
		return self.firstname
