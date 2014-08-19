
Resource estimate based on test batch:
- 92 pages/letters at 3.1 MB, so for 7000 letters estimate 240-260MB.
- It took me 11 mins to record names and addresses (only) for 20 letters, including some Googling. Estimate then 60 to 65 hrs of staff time to enter all (doesn't include VAN entry, but that could be bulk) into the Google doc.
- With batches of 80-100, estimate 70 batches.


Work flow - setup:
- Scan batches of letters to pdfs and have files emailed to Shawn/Aliya. Label each batch with clip and number/letter code.
- Upload batches to Dropbox, put short consistent filename on each, share organizers on entire folder.
- Set up Google doc with cols for filename, page number, name, address, city, state, zip, SD, HD, Senator, HouseRep
- Assign filenames to each staff person


Work flow - data entry:
- Find the filename and corresponding page number for each letter in your batch and enter name and address


Code work - API call to append districts and electeds:
- Export Google doc to csv
- Run Python script to call OpenStates API for each address and add col values for:
	+ SD number
	+ Senator
	+ HD number
	+ House Rep
- Generate file for bad addresses, with reference filename/batch and page number


Code work - pdf sort:
- Use Python script to generate a dictionary of filename + pagenumber values for each HD and SD.
- Run Python script to locate scanned letter by filename and page number and lump into pdfs for each HD and SD
- Print one copy of each PDF per district and clip/label


Code work - dump vol info to Gaytabase or just VAN?
- HD and SD batches: good place from which to start entering phone numbers and emails after address stuff is done
- Dump to regions in gaytabase and/or bulk upload to VAN
