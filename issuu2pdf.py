### issuu2pdf.py
# The aim of this script is to create a PDF
# from ISSUU contents: https://issuu.com
#
### How does it works
# Browse your favorite content on https://issuu.com
# Right click on the first page to display "page information"
# copy thr field "twitter:image" in the url below in the python script.
# remove the "/page_1.jpg" as it is handled by the script.
# Save your modifications of issuu2pdf.py
# Start the script with this command: python issuu2pdf.py
# wait ...
# enjoy your new pdf file
#
### Requiered libraries:
# img2pdf : https://pypi.python.org/pypi/img2pdf
###
import urllib.request
import img2pdf
import sys

imageFiles=[]
# Name of the output PDF file
outputName="issuu.pdf"
i=1
errorMet=False

print("issuu2pdf v0.1")
print("Download %s from https://issuu.com" % outputName)
sys.stdout.flush()

while not errorMet:
    try:
        imageFile="page_%i.jpg" % i
        # URL example to be replaced by yours
        url="https://image.isu.pub/171010072743-33cde5d2d7857b69cda333105aec8929/jpg/%s" % imageFile 

        urllib.request.urlretrieve(url, imageFile)
        imageFiles.append(imageFile)
        print("Retrieved %s from URL %s" % (imageFile, url))
        i+=1
        sys.stdout.flush()
    except:
        errorMet=True

with open(outputName, "wb") as fh:
    fh.write(img2pdf.convert(imageFiles))
