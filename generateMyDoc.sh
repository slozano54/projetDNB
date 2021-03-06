#!/bin/bash

# @author : Sébastien LOZANO

##########################################################################################
#==========> https://pdoc3.github.io/pdoc/
#
#  Script pour générer automatiquement la documentation du package du projet
#==========> docs est le dossier créé qui contiendra la doc HTML
#==========> pyPack est le chemin vers le dossier contenant les modules du projet
#
# Quelques ressources pour écrire les docstrings
#==========> https://numpydoc.readthedocs.io/en/latest/example.html
#==========> https://support.zendesk.com/hc/fr/articles/203691016-Formatage-de-texte-avec-Markdown
#==========> https://realpython.com/documenting-python-code/
#==========> http://sametmax.com/les-docstrings/
#
# La syntaxe markdown fonctionne aussi
#==========> https://www.makeareadme.com/
#==========> https://google.github.io/styleguide/pyguide.html  
#########################################################################################

pdoc --force --html -o docs pyPack