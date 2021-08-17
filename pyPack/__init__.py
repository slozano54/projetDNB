#!/usr/bin/python3
#-*- coding: utf8 -*-

# @author : Sébastien LOZANO

# Source pour l'écriture d'un REAMDE en mardown : https://www.makeareadme.com/ 
# Génère la page d'accueil de la documentation pdoc3

"""
<!-- ![Work in progress](http://www.repostatus.org/badges/latest/wip.svg) -->
![Project Status: Inactive – The project has reached a stable, usable state but is no longer being actively developed; support/maintenance will be provided as time allows.](https://www.repostatus.org/badges/latest/inactive.svg)

_The project has reached a stable, usable state but is no longer being actively developed;_

_Support/maintenance will be provided as time allows._


<!-- PROJECT LOGO -->
<p text-align="center">
  <a href="https://github.com/slozano54/projetDNB">
    <img src="https://raw.githubusercontent.com/slozano54/projetDNB/master/images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h1 text-align="center">PROJET DNB APMEP</h1>
  <h2 text-align="center"> Version initiale - MARS 2021</h2>
  <h3 text-align="center">Auteur - Sébastien LOZANO</h3>

  <p text-align="center">
    <a href="https://github.com/slozano54/projetDNB">Explore the docs</a>
    .    
    <a href="https://github.com/slozano54/projetDNB/issues">Report Bug</a>    
    .
    <a href="https://github.com/slozano54/projetDNB/issues">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#objectif">Objectif</a>
    </li>
    <li>
      <a href="#installation-et-utilisation">Installation et utilisation</a>
    </li>
    <li>
      <a href="#notes">Notes</a>
      <ul>
        <li><a href="#moulinette-ready">Moulinette Ready</a></li>
        <li><a href="#to-update">To update</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>    
  </ol>
</details>

## Objectif
Le projet consistait à récupérer tous les exercices des sujets DNB en partage sur le site de l'APMEP à partir de l'année 2013

La documentation a été générée avec le paquet **pdoc3**.

Utiliser le **package manager** [pip3](https://pip.pypa.io/en/stable/) pour l'installer.

```bash
pip3 install pdoc3
```

## Installation et utilisation
    
La procédure a été testé sous **Linux** uniquement.

* Cloner ce [dépot github](https://github.com/slozano54/projetDNB) ou télécharger [cette archive](https://github.com/slozano54/projetDNB/archive/master.zip).


* à la racine du projet, lancer le script python **programmePrincipal.py**.

```bash
python3 programmePrincipal.py
```

* Sous **Visual Studio Code** lancer Live server et aller dans le dossier **PagesWeb** pour voir la documentation
    
## Notes

### Moulinette Ready 

**Un petit point documentation en guise de pense bête**

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

================ À FAIRE =============

* ~~Supprimer “maitrise de la langue : 4 pts” des lignes des exos~~
* Nettoyer le code
* Factoriser
* Séparer les routines
* ~~Faire une fonction qui liste les fichiers manquants en comparant la liste des fichiers *.text et *.png~~
* Essayer de croper à nouveau pour que les concaténations le soient aussi
* Ajouter un hyperlien vers le dossier des images de l'année concernée https://coopmaths.fr/dnb/ dans chaque exo qui contient une image. QUESTION --> cliquable en png ? ATTENTION en repassant la moulinette à ne pas perdre les tags et à bien conserver les noms actuels des fichiers.
<ul>
<li>Faire une checklist de préparation des fichiers avant passage à la moulinette
<ul>
<li>Renommer les fichiers sources des sujets avec les noms des lieux parmis ... en respectant ... avec le mois en lettres en respectant ...</li>
<li>Remplacer les \section*{Exercice   \subsection*{Exercice  \textbf{\large{Exercice  \textbf{\textsc{Exercice ... etc ...</li>
<li>Replacer les annexes aux bons endroits et supprimer les mots "exercice" etc du texte des annexes</li>
<li>Ajouter le lieu et le mois dans le nom du fichier de façon cohérente</li>
<li>Vérifier le préambule et les paquets spéciaux</li>
<li>Garder les fichiers modifier pour ne pas tout recommencer à chaque fois</li>
<li>Placer tous ces fichiers et les images eps dans le dossier sujets_corrections_tex</li>
<li>Lancer la moulinette</li>
<li>Attention, Ajouter des sauts de lignes après \textbf{Exercice , à la fin du fichier, pas de lignes commentées , ...
<li>Compiler les fichiers du dossier exercices_corrections_tex_autonome correspondant aux fichiers problématiques et adapter le préambule et le fichier source global</li>
</ul>
</li>
</ul>

* Si tout est OK message
<ul>
    <li>Si tout est OK faire en sorte d'avoir en sortie cette structure avec tous les fichiers découpés pour la placer dans le repertoire du depot github des sujets et faire aussi une archive par années avec les fichiers sources globaux et le images :
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


### To update

Pour le moment il faut :

* déposer un sujet au format *.tex dans le dossier **sujets_corrections_tex**

* lancer le script python **programmePrincipal.py**

Pour obtenir :

* La documentation des fonctions du projet dans le dossier **docs/pyPack**

* Un dossier **pagesWeb** avec une démo 

* un fichier *.tex prêt à compiler dans le dossier **tex_a_compiler**

* un fichier pdf compilé dans le dossier **exercices_corrections_pdf**

* un fichier pdf ajusté et compilé dans le dossier **exercices_corrections_pdf_crop**

* un fichier png ajusté dans le dossier **exercices_corrections_png**

* un fichier tex avec le code source de chaque exo ou corrigé dans le dossier **exercices_corrections_tex**


<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/slozano54/projetDNB/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

[MIT](https://choosealicense.com/licenses/mit/)

<!-- CONTACT -->
## Contact

Sébastien LOZANO - Write me on github

Project Link: [https://github.com/slozano54/projetDNB/](https://github.com/slozano54/projetDNB/)

"""
pass