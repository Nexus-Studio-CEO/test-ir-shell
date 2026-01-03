#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module de configuration pour le projet test-ir-shell.
Il contient des fonctions pour installer et configurer le projet.
"""

import os
import sys

def installer_dependances():
    """
    Installe les dépendances nécessaires pour le projet.
    
    :return: None
    """
    os.system("pip install -r requirements.txt")

def configurer_projet():
    """
    Configure le projet en créant les répertoires et les fichiers nécessaires.
    
    :return: None
    """
    os.makedirs("logs", exist_ok=True)
    os.makedirs("data", exist_ok=True)
    with open("config.txt", "w") as fichier:
        fichier.write("Configuration par défaut")

def lancer_projet():
    """
    Lance le projet en exécutant le script principal.
    
    :return: None
    """
    os.system("python main.py")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "install":
            installer_dependances()
        elif sys.argv[1] == "config":
            configurer_projet()
        elif sys.argv[1] == "run":
            lancer_projet()
        else:
            print("Option invalide")
    else:
        print("Utilisation : python setup.py [install|config|run]")