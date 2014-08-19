import csv

# Open the Google doc csv
with open('google_doc_dump.csv', 'rb') as csvfile:
      google_doc_dump_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
      for row in google_doc_dump_reader:
         # Make the API call for each line

         # If there is no match, add batch, page, name, and address to a separate 'not found' file
         # Otherwise, write the HD, SD, legislator information to each cell
      # Write the new csv and call it 'google_doc_dump.csv'
