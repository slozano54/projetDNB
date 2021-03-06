#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
Découper un sujet.

Génèrer le document à compiler, la documentation, les versions pdf, pdf ajustée et png
"""
pass

# On fait les imports nécessaires selon le contexte
# Pour générer la documentation
import os
# Pour mesurer le temps de traitement du script
from datetime import datetime 

# Pour générer tex, pdf,png
import pyPack.compil as compil
import pyPack.html as html

# Script principal
def main():
    # On récupère la date au début du traitement
    start_time = datetime.now()

    # On génère la documentation
    print("=============================================================================")
    print("  Création de la documentation en cours ...  ")    
    print(" ")
    os.system('sh ./generateMyDoc.sh')   

    # On génére le fichier tex
    # On le compile
    # On génère le fichier png
    print("=============================================================================")
    print("  Création du fichier tex, du fichier pdf, du fichier png en cours ...  ")    
    compil.main()

    # On génére page d'accueil
    print("=============================================================================")
    print("  Création de la page d'accueil en cours ...  ")    
    html.main()

    # On évalue le temps de traitement
    end_time = datetime.now()
    print("=============================================================================")
    print("  Durée de traitement : ",end_time-start_time)        
    print("=============================================================================")
 
if __name__ == "__main__":
    main()