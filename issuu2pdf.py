### issuu2pdf.py
# The aim of this script is to create a PDF
# from ISSUU contents: https://issuu.com
#
### How does it works
# Browse your favorite content on https://issuu.com
# Right click on the first page to display "page information"
# copy the field named "twitter:image".
# REMOVE the "page_1.jpg" of the url as it is handled by the script.
# Start the script with 2 arguments: python issuu2pdf.py http://url_of_the_first_page/ destination_file.pdf
# wait ...
# enjoy your new pdf file
#
### Requiered libraries:
# img2pdf : https://pypi.python.org/pypi/img2pdf
###
import os
import sys
import urllib.request
import img2pdf

imageFiles=[]
# Get arguments
# Url of the first page
BaseUrl=sys.argv[1]
# Name of the output PDF file
outputName=sys.argv[2]

i=1
DLerrorMet=False
ULerrorMet=False

print("issuu2pdf v0.3")
print("Download %s from https://issuu.com" % outputName)
sys.stdout.flush()

# DL all images
while not DLerrorMet:
    try:
        imageFile="page_%i.jpg" % i
        url=BaseUrl+imageFile
        urllib.request.urlretrieve(url, imageFile)
        imageFiles.append(imageFile)
        print("Retrieved %s from URL %s" % (imageFile, url))
        sys.stdout.flush()
        i+=1
    except:
        print("DL completed")
        DLerrorMet=True

# Append all images to pdf file
with open(outputName, "wb") as fh:
    fh.write(img2pdf.convert(imageFiles))

# Clean-up temp jpg images
i=1
while not ULerrorMet:
    try:
        imageFile="page_%i.jpg" % i
        os.unlink(imageFile)
        i+=1
    except:
        print("Clean-up completed")
        ULerrorMet=True
print("%s Ready!" % outputName)
print("End")
