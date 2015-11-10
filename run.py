#!/usr/bin/python -O 
# -*- coding: utf-8 -*-
# Projet : kiwi
# Fichier : /data/web/kiwi/run.py 
# Date de création : 7 octobre 2015 (bg)
# Date de modification : 7 octobre 2015 (bg)

#==========< Divers notes >==========
''' Attention de sauvegarder les programmes au format linux.
    Fin de ligne -> LF. '''
    
''' Si le module netifaces n'est pas présent, il convient
    de l'installer avec la commande :
    $ sudo pip install netifaces '''
    
#==========< Importation des modules >==========
import OpenSSL
import netifaces
from dom import views

#==========< Récupération de l'adresse ip >==========
def raspIp():
    interfaces = netifaces.interfaces()
    for i in interfaces:
        #print(i)    #l0, wlan0, eth0
        # on ne traite pas le cas de l'adresse locale
        if i == 'l0':
            continue
        # création d'un dictionnaire contenant les adresses ip pour broadcast, netmask et addr
        iface = netifaces.ifaddresses(i).get(netifaces.AF_INET)
        if iface != None:
            for j in iface:
                #print(j)
                raspIp = j['addr']
    return(raspIp)

#==========< Début du programme >==========
if __name__ == '__main__':
    #context = OpenSSL.SSL.Context(OpenSSL.SSL.SSLv23_METHOD)
    #context = OpenSSL.SSL.Context(OpenSSL.SSL.TLSv1_2_METHOD)
    context = OpenSSL.SSL.Context(OpenSSL.SSL.TLSv1_METHOD)
    context.use_privatekey_file('server.key')
    context.use_certificate_file('server.crt')
    views.app.run(host = raspIp(), port = 8100, ssl_context = context)
    
