import csv
import requests
import pprint
from api_keys import *

# Open the Google doc csv
with open('csvs/google_doc_dump.csv', 'rb') as csvfile, open('csvs/geocoded_letter_data.csv', 'wb') as outfile:
      google_doc_dump_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
      geocodes_writer = csv.writer(outfile, delimiter=',', quotechar='"')
      for index, row in enumerate(google_doc_dump_reader):
       if index>0:
         # Geocode each address with Google Maps API
         address = row[4]+", "+row[5]+", OH "+row[6]
         url = "https://maps.googleapis.com/maps/api/geocode/json?address="+address+"&key="+GOOGLE_GEOCODE_API_KEY
         if row[8] != "":
            lat= "None"
            lng= "None"
         else:
            r = requests.get(url)
            results = r.json()            # Save your answer to results
            lat = results['results'][0]['geometry']['location']['lat']
            lng = results['results'][0]['geometry']['location']['lng']
         geocodes_writer.writerow([row[0],row[1], row[2],row[3],row[4], row[5], row[6], row[7], row[8], lat, lng])
         print lat, lng

with open('csvs/geocoded_letter_data.csv', 'rb') as csvfile, open('csvs/district_data.csv', 'wb') as districtsfile:
     geocoded_letter_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
     district_writer = csv.writer(districtsfile, delimiter=',', quotechar='"')
     for row in geocoded_letter_reader:
         lat = row[9]
         lng = row[10]
         if lat == "None":
            HD="None"
            SD="None"
            Rep="None"
            Sen="None"
         # Make the Sunlight API call for each lat/long pair
         else:
            url = "http://openstates.org/api/v1//legislators/geo/?lat="+str(lat)+"&long="+str(lng)+"&apikey="+SUNLIGHT_API_KEY
            r = requests.get(url)
            results = r.json()
            if results[0]['chamber'] == 'upper':
               HD = results[1]['district']
               Rep = results[1]['last_name']
               SD = results[0]['district']
               Sen = results[0]['last_name']
            else:
               HD = results[0]['district']
               Rep = results[0]['last_name']
               SD = results[1]['district']
               Sen = results[1]['last_name']
            print HD, Rep, SD, Sen
         district_writer.writerow([row[0],row[1], row[2],row[3],row[4], row[5], row[6], row[7], row[8], HD, Rep, SD, Sen])

#Need to add blocks for how to deal with bad addresses and compile a file