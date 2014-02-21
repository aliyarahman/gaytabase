#!/usr/bin/env python

import os
from intelview.models import User, Region, County, SenateDistrict
import csv


#Get regions
NW = Region.objects.get(name = "Northwest")
NE = Region.objects.get(name = "Northeast")
SW = Region.objects.get(name = "Southwest")
SE = Region.objects.get(name = "Southeast")
CENT = Region.objects.get(name = "Central")

#Add SDs

for n in range(1,34):
	SD = SenateDistrict.objects.get_or_create(number = n)[0]
	SD.region =NW
	SD.save()
