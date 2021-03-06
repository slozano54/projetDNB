# !/bin/bash

latex $1.tex || exit
dvips $1.dvi || exit
ps2pdf $1.ps $1.pdf