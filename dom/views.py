#!/usr/bin/python -O 
# -*- coding: utf-8 -*-
# Projet : kiwi
# Fichier : /data/web/kiwi/dom/views.py
# Gestion des pages web
# Date de création : 7 octobre 2015 (bg)
# Date de modification : 7 octobre 2015 (bg)

#==========< Importation des modules >==========
import sys
import flask
import datetime
import globale

#==========< Instanciation >==========
app = flask.Flask(__name__)
#app.config.from_object('dom.globale.ProductConfig')
app.config.from_object('dom.globale.DeveloppementConfig')

#==========< Avant la première requête >==========
@app.before_first_request
def beforeFirstRequest():
    pass
    
#==========< Avant chaque requête >==========
@app.before_request
def beforeRequest():
    ''' Renseigne l'utilisateur de la cession '''
    if 'username' in flask.session:
        flask.g.user = flask.session['username']
    else:
        flask.g.user = None
    print(" =>", flask.g.user)
    return

#==========< Aprés chaque requête >==========
@app.after_request
def afterRequest(response):
    print(" -> Apres", response)
    return(response)

@app.teardown_request
def teardownRequest(exception):
    print(" -> teardown", exception)
    pass
    
#==========< Routage >==========
#----------< Route index.html >----------
@app.route('/')
def index():
    ''' Page d'accueil '''
    if 'username' in flask.session:
        a = globale.PageStartUser()
    else:
        a = globale.PageStart()
    templateDico = a.startDico
    
    return flask.render_template('index.html', **templateDico)

