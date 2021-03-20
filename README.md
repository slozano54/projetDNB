# PROJET DNB APMEP

## Auteur 
Sébastien LOZANO

## Objectif
Le projet consiste \`{a} récupérer tous les exercices des sujets DNB en partage sur le site de l'APMEP \`{a} partir de l'année 2013

Pour le moment le test se fait sur 1 sujet et 1 corrigé

La documentation a été générée avec le paquet **pdoc3**.

Utiliser le **package manager** [pip3](https://pip.pypa.io/en/stable/) pour l'installer.

```bash
pip3 install pdoc3
```

## Installation et utilisation
    
La procédure a été testé sous **Linux** uniquement.

* Cloner ce [dépot github](https://github.com/slozano54/projetDNB) ou télécharger [cette archive](https://github.com/slozano54/projetDNB/archive/master.zip).


* \`{a} la racine du projet, lancer le script python **programmePrincipal.py**.

```bash
python3 programmePrincipal.py
```

* Sous **Visual Studio Code** lancer Live server et aller dans le dossier **PagesWeb** pour voir la documentation
    
## Notes

### Moulinette Ready - un petit point documentation en guise de pense bête
<ul>
<li> Récupérer les fichiers *.tex et *.eps sur https://www.apmep.fr/-Brevet-290-sujets-tous-corriges-
<ul>
<li>soit il n'y a qu'un fichier *.tex </li>
<li>soit il y a une archive *.zip avec un fichier *.tex et des images *.eps</li>
</ul>
<li>Placer tous ces fichiers dans le dossier sujets_corrections_tex de la moulinette</li>
<li>Lancer le script programmePrincipal.py dans un terminal python3 programmePrincipal.py
<ul>
<li>Si le sujet contient des annexes le terminal devient verbeux et donne des instructions, il faut placer manuellement les annexes au bon endroit dans le fichier source *.tex c'est à dire avec l'exercice correspondant avant de poursuivre</li>
<li>Si le lieu et/ou le mois du sujet sont obscurs le terminal devient verbeux aussi et donne des instructions, il s'agit de renommer les fichiers indiqués avec le formatage ad hoc</li>
<li>Sinon ça compile, il suffit de patienter</li>
</ul>
<li>Récupérer les fichiers des exercices et de leur correction 
<ul>
<li>Dans le dossier exercices_corrections_eps : fichier *.eps</li>
<li>Dans le dossier exercices_corrections_pdf : fichier *.pdf grand format</li>
<li>Dans le dossier exercices_corrections_pdf_crop : fichier *.pdf format ajusté</li>
<li>Dans le dossier exercices_corrections_png_jpg : fichier *.png ajusté -- je sais le nom ne correspond pas !</li>
<li>Dans le dossier exercices_corrections_tex : fichier source *.tex sans préambule</li>
<li>Dans le dossier exercices_corrections_tex_autonome : fichier *.tex avec préambule tout prêt à compiler</li>
</ul>
</li>
</ul>

Le programme est sur https://github.com/slozano54/projetDNB

================ A FAIRE =============

* ~~Supprimer “maitrise de la langue : 4 pts” des lignes des exos~~
* Nettoyer le code
* Factoriser
* Séparer les routines
* Faire une fonction qui liste les fichiers manquants en comparant la liste des fichiers *.text et *.png
* Essayer de croper à nouveau pour que les concaténations le soient aussi
<ul>
<li>Faire une checklist de préparation des fichiers avant passage à la moulinette
<ul>
<li>Remplacer les \section*{Exercice   \subsection*{Exercice  \textbf{\large{Exercice  \textbf{\textsc{Exercice ... etc ...</li>
<li>Replacer les annexes aux bons endroits et supprimer les mots exercice etc du texte des annexes</li>
<li>Ajouter le lieu et le mois dans le nom du fichier de façon cohérente</li>
<li>Vérifier le préambule et les paquets spéciaux</li>
<li>Garder les fichiers modifier pour ne pas tout recommencer à chaque fois</li>
</ul>
</li>
</ul>

* Si tout est OK message
<ul>
    <li>Si tout est OK faire en sorte d'avoir en sortie cette structure avec tous les fichiers découpés :
    <ul>
        <li>année
        <ul>
            <li>tex
            <ul>
                <li>eps</li>
                <li>png</li>
            </ul>
            </li>
        </ul>
        </li>
    </ul>
    </li>
</ul>


### À mettre à jour

Cette version n'est qu'un brouillon, elle n'est pas finalisée

Pour le moment il faut :

* déposer un sujet au format *.tex dans le dossier **sujets_corrections_tex**

* lancer le script python **programmePrincipal.py**

Pour obtenir :

* La documentation des fonctions du projet dans le dossier **docs/pyPack**

* Un dossier **pagesWeb** avec une démo 

* un fichier *.tex prêt \`{a} compiler dans le dossier **tex_a_compiler**

* un fichier pdf compilé dans le dossier **exercices_corrections_pdf**

* un fichier pdf ajusté et compilé dans le dossier **exercices_corrections_pdf_crop**

* un fichier png ajusté dans le dossier **exercices_corrections_png**

* un fichier tex avec le code source de chaque exo ou corrigé dans le dossier **exercices_corrections_tex**

