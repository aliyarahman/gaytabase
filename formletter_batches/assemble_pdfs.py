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
      outputfilename = "pdfs/HD"+str(i)+".pdf"
      for b in batchnames:
         input_pdf = PdfFileReader(file("pdfs/"+b, "rb"))
         with open('csvs/district_data.csv', 'rb') as csvfile:
            district_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in district_reader:
               if row[0] == b:
                  if row[11]== str(i):
                    output.addPage(input_pdf.getPage(int(row[1])))
               if output.getNumPages() >0:
                  outputStream = file(outputfilename, "wb")
                  output.write(outputStream)
                  outputStream.close()
                  print "There are %s form letters in %s " % (output.getNumPages(), outputfilename)

'''
# Loop through SenateDistricts
for i in range(1,34):
      output = PdfFileWriter()
      outputfilename = "pdfs/SD"+str(i)+".pdf"
      for b in batchnames:
         input_pdf = PdfFileReader(file("pdfs/"+b, "rb"))
         with open('csvs/district_data.csv', 'rb') as csvfile:
            google_doc_dump = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in google_doc_dump:
               if row[0] == b:
                  if row[13]== str(i):
                     output.addPage(input_pdf.getPage(int(row[1])))
      outputStream = file(outputfilename, "wb")
      output.write(outputStream)
      outputStream.close()
      print "There are %s form letters in %s " % (output.getNumPages(), outputfilename)
'''