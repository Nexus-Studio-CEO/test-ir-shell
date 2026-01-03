#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module principal pour le projet test-ir-shell.

Ce module fournit les fonctionnalités de base pour le shell.
"""

def afficher_aide():
    """
    Affiche l'aide du shell.

    Cette fonction affiche les commandes disponibles dans le shell.
    """
    print("Commandes disponibles :")
    print("  aide      : affiche cette aide")
    print("  quit      : quitte le shell")

def executer_commande(commande):
    """
    Exécute une commande.

    Cette fonction exécute la commande passée en argument.
    Args:
        commande (str): La commande à exécuter.

    Returns:
        str: Le résultat de l'exécution de la commande.
    """
    if commande == "aide":
        afficher_aide()
    elif commande == "quit":
        print("Au revoir !")
        return "quit"
    else:
        print("Commande inconnue")

def lire_commande():
    """
    Lit une commande de l'utilisateur.

    Cette fonction lit une commande de l'utilisateur et la renvoie.
    Returns:
        str: La commande saisie par l'utilisateur.
    """
    return input("shell> ")

if __name__ == "__main__":
    while True:
        commande = lire_commande()
        result = executer_commande(commande)
        if result == "quit":
            break