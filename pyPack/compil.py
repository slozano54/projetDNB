#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
    Génèrer le document à compiler, le compile en pdf, crée un pdf ajusté et un png ajusté
"""
pass

# On fait les imports nécessaires selon le contexte
# Pour générer la documentation, les répertoires, ...
import os
# Pour mesurer le temps de traitement du script
from datetime import datetime 

def generateTex(file : str,source_ex : str):
    """
    Générer un fichier tex prêt à compiler
    """
    #On crée e dossier qui va accueillir les fichiers tex prêts à compiler
    if not os.path.exists("./tex_a_compiler/"):
        os.mkdir("./tex_a_compiler/")

    #On ouvre le fichier dans lequel on va écrire
    myTex = open("./tex_a_compiler/"+file+".tex","w")

    #On ouvre le préambule
    with open("./preambule/preambule.tex","r") as preambule:
        preamb_lines = preambule.read()

    #On ouvre le begin{document}
    with open("./preambule/doc_begin.tex","r") as beginDoc:
        beginDoc_lines = beginDoc.read()

    #On ouvre le fichier source avec les exos
    with open("./exercices_corrections_tex/"+source_ex+".tex","r") as exo:
        exo_lines = exo.read()

    #On ouvre le \end{document}
    with open("./preambule/doc_end.tex","r") as endDoc:
        endDoc_lines = endDoc.read()    

    with myTex as mt:
        mt.write(preamb_lines[0:])
        mt.write(beginDoc_lines[0:])
        mt.write(exo_lines[0:])
        mt.write(endDoc_lines[0:])
    
    #On ferme les fichiers ouverts en écriture
    myTex.close()
    
def compilTexToPDF(source : str):
    """
    Générer le fichier PDF à partir d'un fichier source tex
    """
    #On crée le dossier qui va accueillir les fichiers pdf
    if not os.path.exists("./exercices_corrections_pdf/"):
        os.mkdir("./exercices_corrections_pdf/")
    
    #On lance la commande ce compilation, surement dans le répartoire courant...
    os.chdir("tex_a_compiler")
    os.system("sh compilTex.sh "+source)

    # On se remet à la racine du projet
    os.chdir("../")

def pdf2png(source : str):
    """
    Générer le fichier png ajusté et le pdf ajusté à partir d'un fichier source pdf
    """    
    #On crée le dossier qui va accueillir les fichiers png
    if not os.path.exists("./exercices_corrections_png_jpg/"):
        os.mkdir("./exercices_corrections_png_jpg/")
    
    #On crée le dossier qui va accueillir les fichiers pdf
    if not os.path.exists("./exercices_corrections_pdf_crop/"):
        os.mkdir("./exercices_corrections_pdf_crop/")        
    
    #On lance la commande ce compilation, surement dans le répartoire courant...
    os.chdir("tex_a_compiler")
    os.system("sh dvi2png.sh "+source)

    # On se remet à la racine du projet
    os.chdir("../")

def copyAllFiles(source : str):
    #On copie le fichier pdf
    #os.system("cp "+source+".pdf ../exercices_corrections_pdf/"+source+".pdf" )
    os.system("sh copy.sh ./tex_a_compiler/"+source+".pdf ./exercices_corrections_pdf/"+source+".pdf")

    #On copie le fichier png
    os.system("cp ./tex_a_compiler/"+source+".png ./exercices_corrections_png_jpg/"+source+".png" )

    #On copie le fichier pdf ajusté
    os.system("cp ./tex_a_compiler/"+source+"-crop.pdf ./exercices_corrections_pdf_crop/"+source+"-crop.pdf" )

def cutTex2Ex(file : str,source : str)->list:
    """
    Découpe un fichier source *.tex
    
    file : le début du nom du fichier dans lequel on va écrire
    source : le fichier source contenant les exos
    """

    # On ouvre le fichier source    
    with open("./sujets_corrections_tex/"+source+".tex","r") as source:
        source_lines = source.readlines()

    # Un compteur pour trouver les lignes contenant les entete des exos       
    cpt = 0

    # Un tableau pour les indices contenant le début des exos
    indices = []

    for i in range(len(source_lines)):
        if ("textbf{Exercice" in source_lines[i]):
            indices.append(i)
    indices.append(len(source_lines)) 

    for i in range(len(indices)-1):
        # On ouvre le fichier dans lequel on va écrire
        myTex = open("./exercices_corrections_tex/"+file+"_ex"+str(i+1)+".tex","w")
        # On ajoute les lignes
        myTex.writelines(source_lines[indices[i]:indices[i+1]])
        myTex.close()



       


# Script principal
def main():
    # On récupère la date au début du traitement
    start_time = datetime.now()

    # # On génère le fichier tex à compiler
    # generateTex("test","dnb20Polynesie_ex1")

    # #On compile
    # compilTexToPDF("test")

    # #On convertit en png
    # pdf2png("test")
    
    # #On copie les fichiers pdf, png, pdf-crop dans les bons dossiers
    # copyAllFiles("test")
   
    # Test 
    cutTex2Ex("Brevet_Polynesie_sept_2020_DV","Brevet_Polynesie_sept_2020_DV")

    # On évalue le temps de traitement
    end_time = datetime.now()
    print("=============================================================================")
    print("  Durée de traitement : ",end_time-start_time)        
    print("=============================================================================")
 
if __name__ == "__main__":
    os.system("clear")
    main()