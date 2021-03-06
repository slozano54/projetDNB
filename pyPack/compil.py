#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
    Génèrer le document à compiler, le compile en pdf, crée un pdf ajusté et un png ajusté
"""
pass

# On fait les imports nécessaires selon le contexte
# Pour générer la documentation, les répertoires, ...
import os
# Pour les expressions régulières
import re
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

def cleanPath():
    os.chdir("tex_a_compiler")
    os.system("rm *.aux")
    os.system("rm *.dvi")
    os.system("rm *.log")
    os.system("rm *.out")
    os.system("rm *.png")
    os.system("rm *.ps")
    os.system("rm *.tex")
    os.system("rm *.pdf")
    # On se remet à la racine du projet
    os.chdir("../")


def cutTex2Ex(file : str,source : str)->list:
    """
    Découpe un fichier source *.tex
    
    file : le début du nom du fichier dans lequel on va écrire
    source : le fichier source contenant les exos
    """
    if ("Corrige" in source):
        plus = '_cor'
    else:
        plus = ''
    # On ouvre le fichier source    
    with open("./sujets_corrections_tex/"+source+".tex","r") as source:
        source_lines = source.readlines()
        

    # Un compteur pour trouver les lignes contenant les entete des exos       
    cpt = 0

    # Un tableau pour les indices contenant le début des exos
    indices = []

    for i in range(len(source_lines)):
        # Selon les années la commande pour le style des exos n'est pas la même
        if ("textbf{Exercice" in source_lines[i] or "textbf{\\textsc{Exercice" in source_lines[i]):
            indices.append(i)
    indices.append(len(source_lines)) 
    
    #On crée e dossier qui va accueillir les fichiers tex 
    if not os.path.exists("./exercices_corrections_tex/"):
        os.mkdir("./exercices_corrections_tex/")
    
    for i in range(len(indices)-1):
        # On ouvre le fichier dans lequel on va écrire
        myTex = open("./exercices_corrections_tex/"+file+"_"+str(i+1)+plus+".tex","w")       
        # On ajoute les lignes
        myTex.writelines(source_lines[indices[i]:indices[i+1]])
        myTex.close()

def generateFiles(file : str,source_ex : str):
    """
    Générer tous les fichiers *.pdf *.pdf ajusté *.png *.tex prêt à compiler
    """
    # On génère le fichier tex à compiler
    generateTex(file,source_ex)

    #On compile
    compilTexToPDF(file)

    #On convertit en png
    pdf2png(file)
    
    #On copie les fichiers pdf, png, pdf-crop dans les bons dossiers
    copyAllFiles(file)   

def generateFileName(source_ex : str)->str:
    """
    Générer le nom du fichier pour le découpage au format dnb_aaaa_mm_lieu    
    """
    aaaa = ''
    mm = ''
    lieu = ''   
    
    # Possibles pour les années
    annees = []
    for i in range(2001,datetime.now().year):
        annees.append(i)    
    # On récupère l'année
    for annee in annees:
        if (str(annee) in source_ex):
            aaaa = str(annee)
    
    # Possibles pour les mois
    months = [['jan','01'],['fev','02'],['mars','03'],['avril','04'],['mai','05'],['juin','06'],['juillet','07'],['aout','08'],['sept','09'],['oct','10'],['nov','11'],['dec','12']]
    # On récupère le mois
    for month in months:
        if (month[0] in source_ex):
            mm = month[1]
    if (mm == ''):
        mm = 'bugMois'    

    # Possibles pour les centres
    centres = [
        'pondichery',
        'ameriquesud',
        'ameriquenord',
        'asie',
        'etrangers',
        'metropole',
        'polynesie',
        'caledonie',
    ]
    # On passe le nom du fichier en minuscules
    cleanSource = source_ex.lower()
    # On supprime les underscores
    cleanSource = re.sub('[_]', '', cleanSource)
    # On récupère le lieu
    for centre in centres:
        if (centre in cleanSource):
            lieu = centre
    if (lieu == ''):
        lieu = 'bugLieu'
    
    # On forme le nom du fichier
    filename = "dnb_"+aaaa+"_"+mm+"_"+lieu

    return filename

# Script principal
def main():
    # On génère le fichier tex à compiler
    generateTex("test","dnb20Polynesie_ex1")

    #On compile
    compilTexToPDF("test")

    #On convertit en png
    pdf2png("test")
    
    #On copie les fichiers pdf, png, pdf-crop dans les bons dossiers
    copyAllFiles("test")   

if __name__ == "__main__":    
    os.system("clear")
    # On récupère la date au début du traitement
    start_time = datetime.now()

#    main()
    # Test 
    #cutTex2Ex("Brevet_Polynesie_sept_2020_DV","Brevet_Polynesie_sept_2020_DV")
    #cutTex2Ex("Brevet_Amerique_Nord_juin_2013","Brevet_Amerique_Nord_juin_2013")
    #print(generateFileName("Brevet_Polynesie_sept_2020_DV"))
    #print(generateFileName("Brevet_Amerique_Nord_juin_2013"))
    #cutTex2Ex("Corrige_brevet_Amerique_Nord_mai_2013","Corrige_brevet_Amerique_Nord_mai_2013")
    

    # On évalue le temps de traitement
    end_time = datetime.now()
    print("=============================================================================")
    print("  Durée de traitement : ",end_time-start_time)        
    print("=============================================================================")

