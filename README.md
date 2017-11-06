# issuu_to_pdf
Python script to create a PDF from ISSUU contents

The aim of this python3 script is to create a PDF
from ISSUU contents: https://issuu.com

# How does it works
Browse your favorite content on https://issuu.com
Right click on the first page to display "page information"
copy the field named "twitter:image".
REMOVE the "page_1.jpg" of the url as it is handled by the script.
Start the script with 2 arguments: python issuu2pdf.py http://url_of_the_first_page/ destination_file.pdf
wait ...
enjoy your new pdf file

Python 3.x (NOT 2.x because of urllib compatibility)
Requiered librarie img2pdf : https://pypi.python.org/pypi/img2pdf

Script tested on Windows7/DOS and Linux/Ubuntu 16.04
