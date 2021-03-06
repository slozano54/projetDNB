# !/bin/bash

pdfcrop $1.pdf || exit
pdftoppm $1-crop.pdf|pnmtopng > $1.png