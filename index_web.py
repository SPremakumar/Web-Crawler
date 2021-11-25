#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# PREMAKUMAR Samya
# numéro étudiant : 15600051

import index
import sys

# Fonction principale : contrôle les choix des utilisateurs 
def pilote(source) : 
	index.indexe_bot(source)

	choix = input("""
Maintenant, 
tapez 1 pour chercher un mot en particulier, 
tapez 2 pour chercher tous les mots commencant par une lettre en particulier,
tapez 3 pour enregistrer le dictionnaire dans un fichier,
tapez 4 pour quitter.
Votre choix : """)

	if int(choix) == 1 :
		mots_à_chercher = input('\tTapez un mot : ')  
		index.cherche_mots(mots_à_chercher)

	if int(choix) == 2 : 
		alphabet = input('\tTapez un lettre : ')
		index.alpha(alphabet) 

	if int(choix) == 3 :
		nom = input('\tTaper un nom (suivit de .txt) : ')
		index.write_list_to_file(nom) 

	if int(choix) == 4 : 
		sys.exit()



if len(sys.argv) > 1 :
    for x in sys.argv[1:]: pilote(x)
else : exit('argument manquant : URL ')