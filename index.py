#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# PREMAKUMAR Samya
# numéro étudiant : 15600051

import requests
import re
import time

index = {}
stoplist = "le la les du de des tout tous toutes toute un dedans or donc une par pour ce ça cela qui que quelle dans à ai a au sur se eu mais en ou on an a for in as the this that there when which where with from also it you they on if not all to s of his her or".split()

# Supprime tous les balises HTML
def nettoie_page(page):
    balises = re.compile('<.*?>')
    propre_txt = re.sub(balises, '', page)
    return propre_txt

# Extrait tous les liens d'une page_source :
def extraire_liens(page) :
    response = requests.get(page)                                           
    data = response.text
    html = str(data)                
    links = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', data)      
    liens = list(set().union(links))                           
    return liens

# Extraction d'une page web et supprime tous les balises : 
def get_page(liens):
    try : 
        page = requests.get(liens)
        page = page.text
        page = nettoie_page(page)
        return page
    except Exception :
        pass

# Ajoute les mots dans le dictionnaire 
def ajoute(index, mots, url):
    if mots in index:
        index[mots].append(url)
    else:
        index[mots] = [url]

# Retire toutes les ponctuations
def nettoie(text):
    nv_mots = []
    for mot in text:
        w = re.sub(r'[^\w\s]','',mot)
        w = re.sub(r'\_','',w)
        nv_mots.append(w)
    return nv_mots

# Indexe les pages web 
def indexe(index, url, page):
    if page is None :
        pass  
    
    else : 
        mots = page.lower().split()
        mots = nettoie(mots)

        for mot in mots:
            if mot not in stoplist : 
                ajoute(index, mot, url)

# Unit deux listes : 
def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

# Présentation du dictionnaire : 
def prd(idx):
    for mot in sorted(idx):
        print(mot, ':' , list(set(idx[mot])), '\n' )

# indexe_bot () : indexe la page principale et les liens extraites de la page principale :
def indexe_bot(source):
    dbt_temps = time.time()
    à_indexer = [source]
    visited = []
    
    while à_indexer :
        page = à_indexer.pop(0)
        
        if page not in visited :
            content = get_page(page)
            indexe(index, page, content)
            toute_liens = extraire_liens(source)
            union(à_indexer, toute_liens)
            visited.append(page)
            
    prd(index)
    fin_temps = time.time() - dbt_temps
    print('\n', '\t', """ Merci d'avoir attendu : """, fin_temps)

# Cherche des termes dans le dictionnaire : 
def cherche_mots(mots) :
    mots = mots.split()
    for i in mots : 
        if i.lower() in index:
            print(i, ':', list(set(index[i.lower()]))) # Le set() verifie qu'un lien n'y est pas plusieurs fois 
        else:
            print(" Le(s) terme(s) n'existe pas ")

# Cherche tous les mots commencant par une lettre :
def alpha(lettre) :
    lettre = lettre.split()
    for x in lettre : 
        for i in index :
            if i.startswith(x) : 
                print(i, ':', list(set(index[i])))

# Sauvegarde le dictionnaire dans un fichier : 
def write_list_to_file(filename):
    with open(filename, "w", encoding='utf8') as filename :
        for k, v in index.items() :
            v = list(set(v))
            v = str(v)
            filename.write(k)
            filename.write(':')
            filename.write(v)
            filename.write('\n')
            filename.write('\n')