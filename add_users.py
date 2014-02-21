#!/usr/bin/env python

from django.contrib.auth.models import User

#Add an admin user, two staff users, and a volunteer user
aliya = User(username = "aliya@equalityohio.org", email = "aliya@equalityohio.org", password = "P@ssw0rd123", first_name="Aliya", last_name ="Rahman")
rashida = User(username = "rashida@equalityohio.org", email = "rashida@equalityohio.org", password = "P@ssw0rd123", first_name ="Rashida", last_name ="Davison")
tami = User(username = "tami@equalityohio.org", email = "tami@equalityohio.org", password = "P@ssw0rd123", first_name ="Tami", last_name ="Lunan")
nicole = User(username = "nicole@equalityohio.org", email = "nicole@equalityohio.org", password = "P@ssw0rd123", first_name ="Nicole", last_name ="Thomas")
shawn = User(username = "shawn@equalityohio.org", email = "shawn@equalityohio.org", password = "P@ssw0rd123", first_name ="Shawn", last_name ="Copeland")
elyzabeth = User(username = "elyzabeth@equalityohio.org", email = "elyzabeth@equalityohio.org", password = "P@ssw0rd123", first_name ="Elyzabeth", last_name ="Holford")
grant = User(username = "grant@equalityohio.org", email = "grant@equalityohio.org", password = "P@ssw0rd123", first_name ="Grant", last_name ="Stancliff")
kim = User(username = "kim@equalityohio.org", email = "kim@equalityohio.org", password = "P@ssw0rd123", first_name ="Kim", last_name ="Welter")
volunteer1 = User(username = "volunteer1@equalityohio.org", email = "volunteer1@equalityohio.org", password = "P@ssw0rd123", first_name ="Volunteer", last_name ="One")


aliya.save()
rashida.save()
tami.save()
nicole.save()
shawn.save()
elyzabeth.save()
grant.save()
kim.save()
volunteer1.save()
