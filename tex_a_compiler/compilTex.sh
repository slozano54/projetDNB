# !/bin/bash

#latex $1.tex || exit
# On force la compilation même en cas d'erreur
latex -halt-on-error $1 || exit
dvips $1.dvi || exit
ps2pdf $1.ps $1.pdf