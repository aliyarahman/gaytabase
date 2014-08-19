# This is the pyPdf library. Install with: $ pip install pyPdf
from pyPdf import PdfFileWriter, PdfFileReader
import csv

# Generate a list of batchnames to loop through later
batchnames = []
total_batches = input("How many batches of pdfs do you have?: ")
for i in range(1, total_batches+1):
   batchnames.append("batch"+str(i)+".pdf")

# Loop through HouseDistricts
for i in range(1,100):
      output = PdfFileWriter()
      outputfilename = "HD"+str(i)+".pdf"
      for b in batchnames:
         input_pdf = PdfFileReader(file(b, "rb"))
         with open('google_doc_dump.csv', 'rb') as csvfile:
	    google_doc_dump = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in google_doc_dump:
	       if row[0] == b:
                  if row[7]== i:
	             output.addPage(input_pdf.getPage(int(row[1]))
      outputStream = file(outputfilename, "wb")
      output.write(outputStream)
      outputStream.close()
      print "There are %s form letters in %s " % (output.getNumPages(), outputfilename)


# Loop through SenateDistricts
for i in range(1,34):
      output = PdfFileWriter()
      outputfilename = "SD"+str(i)+".pdf"
      for b in batchnames:
         input_pdf = PdfFileReader(file(b, "rb"))
         with open('google_doc_dump.csv', 'rb') as csvfile:
            google_doc_dump = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in google_doc_dump:
               if row[0] == b:
                  if row[7]== i:
                     output.addPage(input_pdf.getPage(int(row[1]))
      outputStream = file(outputfilename, "wb")
      output.write(outputStream)
      outputStream.close()
      print "There are %s form letters in %s " % (output.getNumPages(), outputfilename)
