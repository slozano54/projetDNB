#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
    Génèrer le document à compiler, le compile en pdf, crée un pdf ajusté et un png ajusté
"""
pass

# Memo couleurs du terminal
# https://chamilo.univ-grenoble-alpes.fr/courses/IUT1RT1M2109/document/1718-Sokoban/build/sequences_ansi.html 


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
    pass
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
    pass
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
    pass    
    #On crée le dossier qui va accueillir les fichiers png
    if not os.path.exists("./exercices_corrections_png/"):
        os.mkdir("./exercices_corrections_png/")
    
    #On crée le dossier qui va accueillir les fichiers pdf
    if not os.path.exists("./exercices_corrections_pdf_crop/"):
        os.mkdir("./exercices_corrections_pdf_crop/")        
    
    #On lance la commande ce compilation, surement dans le répartoire courant...
    os.chdir("tex_a_compiler")
    # os.system("sh dvi2png.sh "+source)
    os.system("sh pdf2png.sh "+source)

    # On se remet à la racine du projet
    os.chdir("../")

def concat_png():
    """
    Concaténer les png si nécessaire    
    """
    pass

    #On lance la commande dans le répertoire adequat
    os.chdir("tex_a_compiler")
    filenames = os.listdir("./")
    #print(listdir)
    # On trie les png
    pngfiles = []
    for filename in filenames:
        if (filename.split('.')[-1] == 'png'):
            pngfiles.append(filename)

    # On nettoie la fin des noms des fichiers
    # on ne garde que ce qui se trouve avant le -
    cleanpngfiles = []
    for pngfile in pngfiles:
        cleanpngfiles.append('-'.join(pngfile.split('-')[:-1]))
    
    # On compte les occurences différentes et les effectifs 
    countpngfiles = []
    for cleanpngfile in cleanpngfiles:
        countpngfiles.append([cleanpngfile,cleanpngfiles.count(cleanpngfile)])

    # On supprime les doublons
    newcountpngfiles = []
    for countpngfile in countpngfiles:
        if (countpngfile not in newcountpngfiles):
            newcountpngfiles.append(countpngfile)
    
    # On concatène ce qu'il faut
    # On crée la chaine du premier argument    
    for i in range(len(newcountpngfiles)):
        firstArgStr = ''
        for j in range(int(newcountpngfiles[i][1])):
            firstArgStr+=newcountpngfiles[i][0]+'-'+str(j+1)+'.png '
            print(firstArgStr)
        # On fait la concaténétion
        print(firstArgStr+newcountpngfiles[i][0]+".png")
        #os.system("sh ./concat_png.sh "+firstArgStr+newcountpngfiles[i][0]+".png")
        os.system("sh concat_png.sh \""+firstArgStr+"\" "+newcountpngfiles[i][0]+".png")
    
    # On supprime les fichiers png qui contiennent un -
    filenames = os.listdir("./")    
    # On trie les png    
    for filename in filenames:
        if (filename.split('.')[-1] == 'png' and '-' in filename):
            os.system("rm "+filename)
    
    # On se remet à la racine du projet
    os.chdir("../")

def copyAllFiles(source : str):
    """
    Copier les fichiers générés là où il faut.
    """
    pass
    #On copie le fichier pdf
    #os.system("cp "+source+".pdf ../exercices_corrections_pdf/"+source+".pdf" )
    os.system("sh copy.sh ./tex_a_compiler/"+source+".pdf ./exercices_corrections_pdf/"+source+".pdf")
    #os.system("cp ./tex_a_compiler/*.pdf ../exercices_corrections_pdf/" )

    #On copie le fichier png
    #os.system("cp ./tex_a_compiler/"+source+".png ./exercices_corrections_png/"+source+".png" )
    os.system("cp ./tex_a_compiler/*.png ./exercices_corrections_png/" )

    #On copie le fichier pdf ajusté
    os.system("cp ./tex_a_compiler/"+source+"-crop.pdf ./exercices_corrections_pdf_crop/"+source+"-crop.pdf" )

    #On crée le dossier qui va accueillir les fichiers tex autonomes
    if not os.path.exists("./exercices_corrections_tex_autonome/"):
        os.mkdir("./exercices_corrections_tex_autonome/")
    #On copie le fichier tex
    os.system("cp ./tex_a_compiler/"+source+".tex ./exercices_corrections_tex_autonome/"+source+".tex" )

    #On crée le dossier qui va accueillir les fichiers eps
    if not os.path.exists("./exercices_corrections_eps/"):
        os.mkdir("./exercices_corrections_eps/")
    #On copie le fichier eps
    os.system("cp ./tex_a_compiler/*.eps ./exercices_corrections_eps/" )

def cleanPath(path):
    """
    Nettoyer les fichiers de compilation inutiles
    """
    pass
    #os.chdir("tex_a_compiler")
    os.chdir(path)
    os.system("rm *.aux")
    os.system("rm *.dvi")
    os.system("rm *.log")
    os.system("rm *.out")
    os.system("rm *.png")
    os.system("rm *.ps")
    os.system("rm *.tex")
    os.system("rm *.pdf")
    os.system("rm *.eps")
    # On se remet à la racine du projet
    os.chdir("../")

def cutTex2Ex(file : str,source : str)->list:
    """
    Découpe un fichier source *.tex
    
    file : le début du nom du fichier dans lequel on va écrire
    source : le fichier source contenant les exos
    """
    pass
    # Est-ce un corrigé ?
    if ("corrige" in source.lower()):
        plus = '_cor'
    else:
        plus = ''
    
    # On copie les fichiers images eps s'il y en a
    print("Copie des fichiers images *.eps s'il y en a ...")
    os.system("cp ./sujets_corrections_tex/*.eps ./tex_a_compiler/" )
    
    # On ouvre le fichier source    
    with open("./sujets_corrections_tex/"+source+".tex","r") as source:
        source_lines = source.readlines()

    # Un tableau pour les indices contenant le début des exos
    indices = []

    # Un tableau avec les textes à chercher dans le code pour repérer les exercices
    strExs = [
        "textbf{Exercice",
        "textbf{\\textsc{Exercice",
        "textbf{EXERCICE",
        "textbf{\\large\\textsc{Exercice",
        "textbf{\\large Exercice"
    ]
    for i in range(len(source_lines)):
        # Selon les années la commande pour le style des exos n'est pas la même        
        for strEx in strExs:
            if (strEx in source_lines[i]):
                indices.append(i)
    indices.append(len(source_lines))

    # On commence par voir s'il y a des annexes
    # S'il y a des annexes on invite à modifier les sources du sujets dans un message d'erreur
    # On vérifie s'il y a ou non le mot annexe dans une ligne du dernier découpage
    # Plutôt dans tout le document Oui c'est mieux !
    isAnnexe = False
    # for i in range(indices[len(indices)-2],indices[len(indices)-1]):
    #     if ("annexe" in source_lines[i].lower()):
    #         isAnnexe = True

    for i in range(indices[0],indices[len(indices)-1]):
        if ("annexe" in source_lines[i].lower()):
            isAnnexe = True
    
    # certaines lignes sont à supprimer des sources
    linesNotTokeep = ["\\end{document}","\\newpage","textbf{Exercice","textbf{\\textsc{Exercice","textbf{EXERCICE","Maîtrise de la langue : 4 points"]
    
    if (isAnnexe):
        print("\033[31m============================= ATTENTION =========================")
        print(" Ce sujet contient des annexes qu'il faut replacer manuellement ")
        print(" au niveau des bons exercices dans le code source du sujet ")
        print(" avant de relancer le traitement.")
        print("\033[33m.................................................................")
        print("Supprimer les références aux exercices dans les annexes en même temps ")
        print("car cela conditionne le découpage des exercices.")
        print(".................................................................\033[31m")
        print(" CELA SIGNIFIE QUE LE SUJET SUIVANT NE SERA DÉCOUPÉ QU'ENSUITE")        
        print("\033[32m"+source.name)        
        print("\033[31m.................................................................\033[0m")
        e=input("Après avoir modifié le fichier source du sujet, appuyer sur une touche \n pour poursuivre la génération des fichiers...")
        print(e)

        # On doit refaire le parcours du fichier sinon on est sur l'ancien découpage !
        # On ouvre le fichier source    
        with open(source.name,"r") as source:
            source_lines = source.readlines()

        # Un tableau pour les indices contenant le début des exos
        indices = []

        for i in range(len(source_lines)):
            # Selon les années la commande pour le style des exos n'est pas la même
            if ("textbf{Exercice" in source_lines[i] or "textbf{\\textsc{Exercice" in source_lines[i] or "textbf{EXERCICE" in source_lines[i]):
                indices.append(i)
        indices.append(len(source_lines))

        if not os.path.exists("./exercices_corrections_tex/"):
            os.mkdir("./exercices_corrections_tex/")
        
        # On génére tous les fichiers sauf le dernier qui peut contenir des annexes
        for i in range(len(indices)-1):
            # On ouvre le fichier dans lequel on va écrire
            myTex = open("./exercices_corrections_tex/"+file+"_"+str(i+1)+plus+".tex","w")       
            # On ajoute les lignes
            for j in range(indices[i],indices[i+1]):
                # On ajoute les lignes sauf \end{document} ou \newpage ou ...
                if ("\\end{document}" not in source_lines[j] and "\\newpage" not in source_lines[j] and "textbf{Exercice" not in source_lines[j] and "textbf{\\textsc{Exercice" not in source_lines[j] and "Maîtrise de la langue : 4 points" not in source_lines[j]):
                #if ("\\end{document}" not in source_lines[j] and "textbf{Exercice" not in source_lines[j] and "textbf{\\textsc{Exercice" not in source_lines[j]):
                    myTex.writelines(source_lines[j])
            myTex.close()
    else:
        #print("OK")
        #On crée le dossier qui va accueillir les fichiers tex 
        if not os.path.exists("./exercices_corrections_tex/"):
            os.mkdir("./exercices_corrections_tex/")
        
        # On génére tous les fichiers sauf le dernier qui peut contenir des annexes
        for i in range(len(indices)-1):
            # On ouvre le fichier dans lequel on va écrire
            myTex = open("./exercices_corrections_tex/"+file+"_"+str(i+1)+plus+".tex","w")       
            # On ajoute les lignes
            for j in range(indices[i],indices[i+1]):
                # On ajoute les lignes sauf \end{document} ou \newpage
                if ("\\end{document}" not in source_lines[j] and "\\newpage" not in source_lines[j] and "textbf{Exercice" not in source_lines[j] and "textbf{\\textsc{Exercice" not in source_lines[j] and "Maîtrise de la langue : 4 points" not in source_lines[j]):
                #if ("\\end{document}" not in source_lines[j]  and "textbf{Exercice" not in source_lines[j] and "textbf{\\textsc{Exercice" not in source_lines[j]):
                    myTex.writelines(source_lines[j])
            myTex.close()
    
    # #On crée e dossier qui va accueillir les fichiers tex 
    # if not os.path.exists("./exercices_corrections_tex/"):
    #     os.mkdir("./exercices_corrections_tex/")
    
    # # On génére tous les fichiers sauf le dernier qui peut contenir des annexes
    # for i in range(len(indices)-2):
    #     # On ouvre le fichier dans lequel on va écrire
    #     myTex = open("./exercices_corrections_tex/"+file+"_"+str(i+1)+plus+".tex","w")       
    #     # On ajoute les lignes
    #     myTex.writelines(source_lines[indices[i]:indices[i+1]])
    #     myTex.close()
    
    # # On vérifie s'il y a ou non le mot annexe dans une ligne
    # isAnnexe = False
    # for i in range(indices[len(indices)-2],indices[len(indices)-1]):
    #     if ("annexe" in source_lines[i].lower()):
    #         isAnnexe = True

    # # Si il y a des annexes on renomme
    # if (isAnnexe):
    #     # On ouvre le fichier dans lequel on va écrire
    #     myTex = open("./exercices_corrections_tex/"+file+"_"+str(len(indices)-1)+plus+"avecLesAnnexes.tex","w")       
    #     # On ajoute les lignes
    #     for i in range(indices[len(indices)-2],indices[len(indices)-1]):
    #         # On ajoute les lignes sauf \end{document}
    #         if ("\\end{document}" not in source_lines[i]):
    #             myTex.writelines(source_lines[i])
    #     #myTex.writelines(source_lines[indices[len(indices)-2]:indices[len(indices)-1]])
    #     myTex.close()
        
def generateFiles(file : str,source_ex : str):
    """
    Générer tous les fichiers *.pdf *.pdf ajusté *.png *.tex prêt à compiler
    """
    pass
    # On génère le fichier tex à compiler
    generateTex(file,source_ex)

    #On compile
    compilTexToPDF(file)

    #On convertit en png
    pdf2png(file)

    # On concatène les png à concaténer
    concat_png()
        
    #On copie les fichiers pdf, png, pdf-crop dans les bons dossiers
    copyAllFiles(file)   

def generateFileName(source_ex : str)->str:
    """
    Générer le nom du fichier pour le découpage au format dnb_aaaa_mm_lieu
    """
    pass
    aaaa = ''
    mm = ''
    lieu = ''   
    
    # Possibles pour les années
    annees = []
    for i in range(2001,datetime.now().year+1):
        annees.append(i)    
    # On récupère l'année
    for annee in annees:
        if (str(annee) in source_ex):
            aaaa = str(annee)
    
    # Possibles pour les mois
    months = [['jan','01'],['fev','02'],['mars','03'],['avril','04'],['mai','05'],['juin','06'],['juillet','07'],['aout','08'],['sept','09'],['oct','10'],['nov','11'],['dec','12']]
    # On récupère le mois
    for month in months:
        if (month[0] in source_ex.lower()):
            mm = month[1]        
    if (mm == ''):
        mm = 'bugMois'    

    # Possibles pour les centres
    centres = [
        'pondichery',
        'ameriquesud',
        'amdusud',
        'amdusudsecours',
        'ameriquenord',
        'ameriquedunord',
        'amdunord',
        'asie',        
        'etrangers',
        'etranger',
        'maroc',        
        'metropole',
        'polynesie',
        'caledonie',
        'wallis',
        'antillesguyane',
        'antilles',
        'grece',                
        'sujet0', # pour le bac
        'sujet1', # pour le bac
        'sujet2',  # pour le bac
        'specimen1', # pourE3C
    ]

    # On passe le nom du fichier en minuscules
    cleanSource = source_ex.lower()
    # On supprime les underscores et les -
    cleanSource = re.sub('[_-]', '', cleanSource)
    # On récupère le lieu
    for centre in centres:
        if (centre in cleanSource):
            if centre == 'amdunord' or centre == 'ameriquedunord':
                lieu = 'ameriquenord'
            elif centre == 'amdusud':
                lieu = 'ameriquesud'                
            elif centre == 'wallis':
                lieu = 'wallisfutuna'
            elif (centre == 'antilles' or centre =='antillesguyane'):
                #lieu = 'antillesguyane'
                lieu = 'metropole'
            elif (centre =='etranger' or centre =='etrangers'):
                lieu = 'etrangers'
            elif (centre == 'maroc'):
                lieu ='etrangers_maroc'
            else:
                lieu = centre
    if (lieu == ''):
        lieu = 'bugLieu'
    
    # On forme le nom du fichier
    if ('brevet' in cleanSource):    
        filename = "dnb_"+aaaa+"_"+mm+"_"+lieu
    if ('bac' in cleanSource):
        filename = "bac_"+aaaa+"_"+mm+"_"+lieu
    if ('e3c' in cleanSource):
        filename = "e3c_"+aaaa+"_"+mm+"_"+lieu
    
    return filename

if __name__ == "__main__":    
    os.system("clear")
    # On récupère la date au début du traitement
    start_time = datetime.now()

    # Test 
    #cutTex2Ex("Brevet_Polynesie_sept_2020_DV","Brevet_Polynesie_sept_2020_DV")
    #cutTex2Ex("Brevet_Amerique_Nord_juin_2013","Brevet_Amerique_Nord_juin_2013")
    #print(generateFileName("Brevet_Polynesie_sept_2020_DV")
    #print(generateFileName("Brevet_Amerique_Nord_juin_2013")
    #cutTex2Ex("Corrige_brevet_Amerique_Nord_mai_2013","Corrige_brevet_Amerique_Nord_mai_2013")   
    # gestion des couleurs   
    #cutTex2Ex("wallis","Brevet_Wallis_2_dec_2017")
    #concat_png()
    print(generateFileName('Brevet-Amerique-Sud-dec-2015'))
    print(generateFileName('Bac-Amerique-Sud-dec-2015'))
    print(generateFileName('Bac_sujet0_juin_2021_DV'))
    print(generateFileName('Corrige_Bac_sujet0_juin_2021_DV'))    
    
    # On évalue le temps de traitement
    end_time = datetime.now()
    print("=============================================================================")
    print("  Durée de traitement : ",end_time-start_time)        
    print("=============================================================================")

