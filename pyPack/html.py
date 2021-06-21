#!/usr/bin/python3
#-*- coding: utf8 -*-

# @author : Sébastien LOZANO
"""
    Génère une page HTML.
"""
pass

# On fait les imports nécessaires selon le contexte
# Pour pouvoir créer un répertoire, ici pour y mettre les fichiers HTML
import os

# On fait les imports nécessaires selon le contexte
# Pour générer les fichiers HTML 
if __name__ == "__main__":    
    from HTML_constantes import *
else:
    from pyPack.HTML_constantes import *

############################################################################################################
# Générer le fichier pagesWeb/index.HTML
############################################################################################################

def main():
    """
        Fonction principale qui sera appelée pour générer l'ensemble des pages HTML.    
    """
    pass

    # On remonte d'un niveau
    #os.chdir("../")

    # On crée le dossier qui va accueillir les fichiers HTML si il n'existe pas
    if not os.path.exists("./pagesWeb/"):
        os.mkdir("./pagesWeb/")

    # On ouvre en écriture le fichier html qui va recevoir le code
    indexHTML = open("./pagesWeb/index.html", "w")    
    
    # On ajoute le doctype et le head
    for elt in docTypeHeadStyle:
        indexHTML.writelines(elt)
    
    # On ouvre le body
    indexHTML.writelines(["<body>\n"])

    # On ajoute les éléments de la barre de navigation
    for elt in barreDeNavigation:
        indexHTML.writelines(elt)  
    
    # On ajoute une partie spécifique
    indexHTML.writelines([
        """
        <h2>ACCUEIL</h2>\n
        <p> Le projet consiste à récupérer tous les exercices des sujets DNB en partage sur le site de l'APMEP<br>
        Pour le moment le test se fait sur le premier exo du sujet de polynésie 2020<br><br>
        Pour générer la documentation il faut installer le paquet python <a href="https://pdoc3.github.io/pdoc/" target="_blank"> pdoc3</a>
        </p>
        
        <h3>Auteur</h3>
        <p>Sébastien LOZANO</p>

        <h3> Installation et utilisation </h3>        
        <p>La procédure a été testé sous <b>Linux</b> uniquement.
        <ul>
        <li>Télécharger cette <a href="https://github.com/slozano54/projetDNB/archive/master.zip"> archive zip</a></li>
        <li>Décompresser l'archive</li>
        <li>Déposer un sujet au format *.tex dans le dossier <b>sujets_corrections_tex</b></li>        
        <li>Lancer le script python <b>programmePrincipal.py</b> à la racine du projet.</li>
        <li>Sous <b>Visual Studio Code</b> lancer Live server et aller dans le dossier <b>PagesWeb</b> et lancer index.html</li>
        </ul>
        </p>          

        <h3> Notes </h3>
        <p>
        Les fichiers de la documentations sont générés dans le dossier <b>docs/pyPack</b><br><br>
        Les fichiers HTML sont générés dans le dossier <b>pagesWeb</b><br><br>
        <a class="navButton" href="../exercices_corrections_pdf/" target="_blank"><span>voir les fichiers pdf</span></a>
        <a class="navButton" href="../exercices_corrections_pdf_crop/" target="_blank"><span>voir les fichiers pdf ajustés</span></a>
        <a class="navButton" href="../exercices_corrections_png/" target="_blank"><span>voir les fichiers png ajustés</span></a>
        <br>   
        <a class="navButton" href="https://www.overleaf.com/docs?snip_uri=https://mathslozano.fr/mathaleaProjetDNB/tex_a_compiler/dnb_2013_04_pondichery_1.tex&engine=latex_dvipdf" target="_blank"><span>compiler un fichier tex sur overleaf</span></a>        
        <a class="navButton" href="../tex_a_compiler/dnb_2013_04_pondichery_1.tex" target="_blank"><span>télécharger le fichier source tex </span></a>
        </p>

        <h3> License <a href="https://choosealicense.com/licenses/mit/" target="_blank">MIT</a><h3>        
        """        
    ])
    
    # On ferme le body
    indexHTML.writelines([
    """    
    </body>\n
    </html>\n
    """
    ])
    
    #On ferme le fichier
    indexHTML.close()

if __name__ == "__main__":
    main()