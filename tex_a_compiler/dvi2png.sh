# !/bin/bash

# pour ces commandes
######### MAC OS ############
#brew install netpbm
#brew install poopler
######### Linux #############
# Je ne sais plus
# poopler-utils ?
#http://netpbm.sourceforge.net/doc/pnmtopng.html
#https://tex.stackexchange.com/questions/11866/compile-a-latex-document-into-a-png-image-thats-as-short-as-possible

pdfcrop -margin 3 $1.pdf || exit
#pdftoppm $1-crop.pdf|pnmtopng -compression 0 > $1.png
pdftoppm -r 300 $1-crop.pdf|pnmtopng -compression 0 > $1.png
