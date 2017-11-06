# issuu_to_pdf
Python script to create a PDF from ISSUU contents</br>

The aim of this python3 script is to create a PDF</br>
from ISSUU contents: https://issuu.com

# How does it works
Browse your favorite content on https://issuu.com</br>
Right click on the first page to display "page information"</br>
copy the field named "twitter:image".</br>
REMOVE the "page_1.jpg" of the url as it is handled by the script.</br>
Start the script with 2 arguments: python issuu2pdf.py http://url_of_the_first_page/ destination_file.pdf</br>
wait ...</br>
enjoy your new pdf file</br>
</br>
Python 3.x (NOT 2.x because of urllib compatibility)</br>
Requiered librarie img2pdf : https://pypi.python.org/pypi/img2pdf</br>
</br>
Script tested on Windows7/DOS and Linux/Ubuntu 16.04</br>
