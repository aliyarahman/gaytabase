import csv
import requests
import pprint
from api_keys import *

# Open the Google doc csv
with open('csvs/google_doc_dump.csv', 'rb') as csvfile:
      google_doc_dump_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
      for index, row in enumerate(google_doc_dump_reader):
       if index>0:
        if row[8] != "":
         print "Not in Ohio"
        else:
         # Geocode each address with Google Maps API
         address = row[4]+", "+row[5]+", OH "+row[6]
         url = "https://maps.googleapis.com/maps/api/geocode/json?address="+address+"&key="+GOOGLE_GEOCODE_API_KEY
         r = requests.get(url)
         results = r.json()		# Save your answer to results
         lat = results['results'][0]['geometry']['location']['lat']
         lng = results['results'][0]['geometry']['location']['lng']
         print lat, lng
         # If there is no match, add batch, page, name, and address to a separate 'not geocoded' file
         # Otherwise, write latitude and longitude coordinates to a new .csv in row[7] and row[8] respectively
         # NEED TO FINISH WRITE PORTION

#with open('csvs/geocoded_letter_data.csv', 'rb') as csvfile:
#     geocoded_letter_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
#      for row in geocoded_letter_reader:
#         lat = row[7]
#         lng = row[8]
         # Make the Sunlight API call for each lat/long pair
#         url = "http://openstates.org/api/v1//legislators/geo/?lat="+str(lat)+"&long="+str(lng)+"&apikey="+SUNLIGHT_API_KEY
#         r = requests.get(url)
#         state_legislators = r.json()
         # If there is no match, add batch, page, name, and address to a separate 'not found' file
         # Otherwise, write the HD, SD, legislator information to each cell
         # Write the new csv and call it 'google_doc_dump.csv'
         # NEED TO FINISH WRITE PORTION

