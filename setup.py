#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module de configuration pour le projet test-ir-shell.
"""

def configurer_projet():
    """
    Configure le projet en créant les répertoires nécessaires.

    Returns:
        None
    """
    import os
    repertoire_projet = "test-ir-shell"
    if not os.path.exists(repertoire_projet):
        os.makedirs(repertoire_projet)

def installer_dependances():
    """
    Installe les dépendances nécessaires pour le projet.

    Returns:
        None
    """
    import subprocess
    subprocess.run(["pip", "install", "-r", "requirements.txt"])

def lancer_projet():
    """
    Lance le projet en exécutant le script principal.

    Returns:
        None
    """
    import subprocess
    subprocess.run(["python", "main.py"])

if __name__ == "__main__":
    configurer_projet()
    installer_dependances()
    lancer_projet()