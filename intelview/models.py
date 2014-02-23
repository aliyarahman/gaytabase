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
	DPI = models.CharField(max_length=7, default = [])
	cities = models.ManyToManyField(City, default = [])
	counties = models.ManyToManyField(County, default = [])
	
	def __unicode__(self):
		return self.shortcode


class HouseDistrict(models.Model):
	number = models.IntegerField()
	shortcode = models.CharField(max_length=4)
	region = models.ForeignKey(Region)
	nestedInSD = models.ForeignKey(SenateDistrict)
	DPI = models.CharField(max_length=7, default = [])
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
	donors = models.CharField(max_length=400, default = "")
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
	donors = models.CharField(max_length=400, default = "")
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
		return self.shortcode


class Business(models.Model):
	name = models.CharField(max_length=45, unique = True)
	description = models.CharField(max_length=400)
	LGBTowned = models.IntegerField(max_length=1, default = 2)
	#LGBTowned codes for businesses: #0 = No, #1 = Yes, #2 = Unknown
	CEO = models.CharField(max_length=400)
	peopleConnections = models.CharField(max_length=400)
	regions = models.ManyToManyField(Region)
	counties = models.ManyToManyField(County, default = [])
	cities = models.ManyToManyField(City)
	inSDs = models.ManyToManyField(SenateDistrict)
	inHDs = models.ManyToManyField(HouseDistrict)
	donatedToSenators = models.ManyToManyField(Senator)
	donatedToSenators = models.ManyToManyField(Representative)
	signedENDA = models.IntegerField(max_length=1)
	jobsOhio =models.IntegerField(max_length=1)
	hasSOnondiscrim = models.IntegerField(max_length=1)
	hasGInondiscrim = models.IntegerField(max_length=1)
	hasSSDPBenefits = models.IntegerField(max_length=1)
	HRCscore = models.IntegerField(max_length=3)
	otherNotes = models.CharField(max_length=400)

	def __unicode__(self):
		return self.name


class Organization(models.Model):
	name = models.CharField(max_length=45, unique = True)
	LocalStateNationalAffinity = models.CharField(max_length=40)
	description = models.CharField(max_length=400)
	ally = models.IntegerField(max_length=1)
# add column for affinity group
# add column for conservative
# add column for nonprofit
	primaryContact = models.CharField(max_length=400)
	regions = models.ManyToManyField(Region)
	counties = models.ManyToManyField(County, default = [])
	cities = models.ManyToManyField(City)
	inSDs = models.ManyToManyField(SenateDistrict)
	inHDs = models.ManyToManyField(HouseDistrict)
	otherNotes = models.CharField(max_length=400)		
	def __unicode__(self):
		return self.name


class Leader(models.Model):
	firstname = models.CharField(max_length=400)
	lastname = models.CharField(max_length=400)
	tite= models.CharField(max_length=400)
	email = models.CharField(max_length=45)
	phone = models.CharField(max_length=400)
	address = models.CharField(max_length=400)
	cities = models.ManyToManyField(City)
	county = models.ForeignKey(County)
	region = models.ForeignKey(Region)
	inSD = models.ForeignKey(SenateDistrict)
	inHD = models.ForeignKey(HouseDistrict)
	communityleader = models.IntegerField(max_length=1)
	faithleader = models.IntegerField(max_length=1)
	volunteerleader = models.IntegerField(max_length=1)
	denomination = models.CharField(max_length=400)
	organizations = models.ManyToManyField(Organization)
	otherNotes = models.CharField(max_length=400)
	
	def __unicode__(self):
		return self.firstname
		
