#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module principal du projet test-ir-shell.

Ce module fournit les fonctionnalités de base pour le projet test-ir-shell.
Il contient des fonctions pour la gestion des commandes et des réponses.
"""

def execute_commande(commande):
    """
    Exécute une commande et retourne la sortie.

    Args:
        commande (str): La commande à exécuter.

    Returns:
        str: La sortie de la commande.
    """
    import subprocess
    return subprocess.check_output(commande, shell=True).decode("utf-8")

def parse_reponse(reponse):
    """
    Parse une réponse et retourne les informations extraites.

    Args:
        reponse (str): La réponse à parser.

    Returns:
        dict: Les informations extraites de la réponse.
    """
    import json
    try:
        return json.loads(reponse)
    except json.JSONDecodeError:
        return {}

def affiche_aide():
    """
    Affiche l'aide pour le projet test-ir-shell.
    """
    print("Aide pour le projet test-ir-shell")
    print("-------------------------------")
    print("Commandes disponibles :")
    print("  - execute_commande : exécute une commande")
    print("  - parse_reponse : parse une réponse")

if __name__ == "__main__":
    affiche_aide()
    commande = input("Entrez une commande : ")
    reponse = execute_commande(commande)
    informations = parse_reponse(reponse)
    print("Informations extraites :")
    print(informations)