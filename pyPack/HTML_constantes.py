#!/usr/bin/python3
#-*- coding: utf8 -*-

# @author : Sébastien LOZANO

"""
  Générer les parties communes aux fichiers HTML.

  On met les constantes dans des chaînes.
"""
pass

docTypeHead = (
  """
<!doctype html>
<html lang=\"fr\">
<head>
    <meta charset=\"UTF-8\">
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">    
    <title>DNB-APMEP-MATHALEA</title>
</head>
"""
)

style = (
  """
<style>

</style>
"""
)

docTypeHeadStyle = (
  """
<!doctype html>
<html lang=\"fr\">
<head>
    <meta charset=\"UTF-8\">
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">    
    <title>Projet DNB APMEP MATHALEA</title>
    <style>
      .navButton {
        display: inline-block;
        border-radius: 4px;
        background-color: #ff7f00;
        color: #FFFFFF;
        text-align: center;
        font-size: 1rem;
        padding: 0.75rem;
        width: auto;
        transition: all 0.5s;
        margin: 0.3rem;
      }
      .navButton {
        font-weight: bold;
      }
      .navButton {
        border: none;
        cursor: pointer;
      }
      .navButton span {
        cursor: pointer;
        display: inline-block;
        position: relative;
        transition: 0.5s;
      }
      .navButton span:after {
        content: '\\00bb';
        position: absolute;
        opacity: 0;
        top: 0;
        right: -1.25rem;
        transition: 0.5s;
      }

      .navButton:hover span {
        padding-right: 1.5rem;
      }
      .navButton:hover span:after {
        opacity: 1;
        right: 0;
      }
    </style>
</head>
"""
)

barreDeNavigation = (
  """
<h1>PROJET DNB APMEP MATHALEA</h1>
<hr>
<h4>Source des données : <a href=\"https://www.apmep.fr/-Brevet-289-sujets-tous-corriges-\" target=\"_blank\">https://www.apmep.fr/-Brevet-289-sujets-tous-corriges-</a></h4>
<hr>
<a class="navButton" href=\"index.html\" target=\"_self\"><span>Accueil</span></a>
<a class="navButton" href=\"../docs/pyPack/index.html\" target=\"_blank\"><span>Documentation</span></a>
<hr>
"""
)