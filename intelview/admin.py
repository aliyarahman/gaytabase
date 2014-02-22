from django.contrib import admin
from intelview.models import User, Region, County, City, SenateDistrict, HouseDistrict, Senator, Representative, Business, Organization, Leader


# Register your models here.
admin.site.register(Region)
admin.site.register(County)
admin.site.register(City)
admin.site.register(SenateDistrict)
admin.site.register(HouseDistrict)
admin.site.register(Senator)
admin.site.register(Representative)
admin.site.register(Business)
admin.site.register(Organization)
admin.site.register(Leader)
