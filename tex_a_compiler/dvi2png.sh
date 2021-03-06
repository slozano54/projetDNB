# !/bin/bash

# pour ces commandes
######### MAC OS ############
#brew install netpbm
#brew install poopler
######### Linux #############
# Je ne sais plus

pdfcrop $1.pdf || exit
pdftoppm $1-crop.pdf|pnmtopng -compression 0 > $1.png