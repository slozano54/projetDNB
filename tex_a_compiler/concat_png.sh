# !/bin/bash

# https://stackoverflow.com/questions/20075087/how-to-merge-images-in-command-line
# de droite à gauche
pnmcat -lr <(pngtopnm 1.png) <(pngtopnm 2.png) | pnmtopng > all.png
# de haut en bas
pnmcat -tb <(pngtopnm 1.png) <(pngtopnm 2.png) | pnmtopng > all.png