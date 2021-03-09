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
############################################
# conversion png mais sortie trop lourde
#pdftoppm $1-crop.pdf|pnmtopng -compression 0 > $1.png
#pdftoppm -r 300 $1-crop.pdf|pnmtopng -compression 0 > $1.png
#pdftoppm -r 300 $1-crop.pdf|pnmtopng > $1.png
pdftoppm -f 1 -l 2 -r 300 -png $1-crop.pdf $1
##################################
# conversion png avec convert
#convert -density 300 -antialias $1-crop.pdf -quality 100 -alpha remove $1.png
#convert -density 300 -antialias $1-crop.pdf -quality 100 -colorspace RGB $1.png