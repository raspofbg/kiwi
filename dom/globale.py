#!/usr/bin/python -O 
# -*- coding: utf-8 -*-
# Projet : kiwi
# Fichier : /data/web/kiwi/dom/globale.py
# Date de création : 7 octobre 2015 (bg)
# Date de modification : 7 octobre 2015 (bg)

#==========< Importation des modules >==========
import os

#==========< Définition des classes >==========
#----------< Configuration de Flask >----------
class Config(object):
    ''' Concerne la configuration standard '''
    DEBUG = False               # Invalide le mode débuggage
    CSRF_ENABLED = True         # Sécurise l'application
    SECRET_KEY = os.urandom(24) # Génération aléatoire d'une clef de 24 caractères
    
class ProductConfig(Config):
    ''' Classe identique à Config '''
    pass
    
class DeveloppementConfig(Config):
    ''' Classe héritant de Config '''
    DEBUG = True
    print(' -> Débuggage actif')
    
#----------< Pour l'ensemble des pages >----------
class Page(object):
    ''' Concerne l'ensemble des pages html et des variables globales '''
    def __init__(self):
        self.path = "/data/web/kiwi/dom"
        self.titre = "Kiwi"
        self.version = "0.00.a"
        self.nomBase = "domo"

#----------< Page d'accueil avant connexion >----------
class PageStart(object):
    ''' Concerne la page d'accueil '''
    def __init__(self):
        a = Page()
        self.startMenu = ['Accueil',
                          'Connexion',
                          'Informations']
        self.startMenuList = {self.startMenu[0] : '/',
                              self.startMenu[1] : 'login.html',
                              self.startMenu[2] : '/info.html'}
        self.startDico = {'title' : a.titre,
                          'version' : a.version,
                          'pageTitle' : 'Accueil',
                          'menu' : self.startMenu,
                          'menuList' : self.startMenuList}
                          
