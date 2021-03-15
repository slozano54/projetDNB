#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
Découper un sujet.

Génèrer le document à compiler, la documentation, les versions pdf, pdf ajustée et png
"""

__author__      = "Sébastien Lozano"
__licence__   = "MIT"

pass

# On fait les imports nécessaires selon le contexte
# Pour générer la documentation
import os
# Pour mesurer le temps de traitement du script
from datetime import datetime 

# Pour générer tex, pdf,png
import pyPack.compil as compil
import pyPack.html as html

# Pour tester s'il manque des fichiers
def isAnyBug():
    """
    Pour tester s'il y a eu des bugs de compilation.
    On compare les fichiers du dossier **exercices_corrections_png** et du  dossier **exercices_corrections_tex**
    """
    pass

    if (not os.path.exists("./exercices_corrections_png/")) or (not os.path.exists("./exercices_corrections_tex/")):
        print("Les dossiers  pour les png et/ou les tex n'existent pas")
    else:
        #On lance la commande dans le répertoire adequat
        os.chdir("exercices_corrections_png")
        filenames = os.listdir("./")        
        # On trie les png
        pngfiles = []
        for filename in filenames:
            if (filename.split('.')[-1] == 'png'):
                pngfiles.append(filename.split('.')[0])
        
        #On lance la commande dans le répertoire adequat
        os.chdir("../exercices_corrections_tex")
        filenames = os.listdir("./")        
        # On trie les png
        texfiles = []
        for filename in filenames:
            if (filename.split('.')[-1] == 'tex'):
                texfiles.append(filename.split('.')[0])
        print(pngfiles)
        print(len(pngfiles))
        print(texfiles)
        print(len(texfiles))
        #On teste déjà les cardinaux
        if (len(pngfiles) != len(texfiles)):
            print("BUG")
            bugfiles = []
            for texfile in texfiles:
                if (texfile not in pngfiles):
                    bugfiles.append(texfile)
            print("Fichiers probématiques : ",bugfiles)

 
# Script principal
def main():
    # On récupère la date au début du traitement
    start_time = datetime.now()

    # On génère la documentation
    print("=============================================================================")
    print("  Création de la documentation en cours ...  ")    
    print(" ")
    os.system('sh ./generateMyDoc.sh')   

    # On découpe le sujet en exos
    # Pour chaque exos
    # On génére le fichier tex
    # On le compile
    # On génère le fichier png
    print("")
    print("=============================================================================")
    print("  Création des fichiers tex, pdf, png en cours ...  ")    
    #compil.main()
    #compil.generateFiles("dnb20Polynesie_ex1","dnb20Polynesie_ex1")
    # On découpe les sujets présents dansle dossiers sujets_corrections_tex
    for (dirpath, dirnames, filenames) in os.walk('./sujets_corrections_tex/'):        
        for source in filenames:
            #On ne traite que les sources pas les images ou le fichier .gitkeep
            if (source.split('.')[-1] != 'eps' and source.split('.')[-1] != 'txt' and source != ".DS_Store"):
                # On supprime l'extension du fichier
                source = '.'.join(source.split('.')[:-1])            
                # On formatte le nom du fichier de sortie
                source_format = compil.generateFileName(source)
                if ('bugMois' in source_format or 'bugLieu' in source_format):
                    print("\033[31m============================= ATTENTION =========================")
                    print("Problème avec le nom du fichier : \033[32m"+source+"\033[31m")
                    print("La sortie actuelle est : \033[32m"+source_format+"\033[31m")
                    print(".................................................................\033[0m")
                    source_format = input("Renommez le correctement selon la nomenclature dnb_aaaa_mm_lieu\n")                
                # On découpe
                compil.cutTex2Ex(source_format,source) 
           
    # Tous les fichiers du répertoire /exercices_corrections_tex
    for (dirpath, dirnames, filenames) in os.walk('./exercices_corrections_tex/'):
        for source in filenames:            
            # On supprime l'extension du fichier
            source = '.'.join(source.split('.')[:-1])                        
            compil.generateFiles(source,source)
    
    # On nettoie le dossier tex_a_compiler
    compil.cleanPath("tex_a_compiler")

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
    os.system("clear")
    main()
    os.system("clear")
    isAnyBug()