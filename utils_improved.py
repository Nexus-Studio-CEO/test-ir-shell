#!/usr/bin/env python3
# coding: utf-8

"""
Module utils_improved pour le projet test-ir-shell.

Ce module fournit des fonctions utilitaires pour le traitement de données et la gestion de fichiers.
"""

def lire_fichier(nom_fichier):
    """
    Lit le contenu d'un fichier.

    Args:
        nom_fichier (str): Nom du fichier à lire.

    Returns:
        str: Contenu du fichier.
    """
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            return fichier.read()
    except FileNotFoundError:
        return None

def ecrire_fichier(nom_fichier, contenu):
    """
    Écrit du contenu dans un fichier.

    Args:
        nom_fichier (str): Nom du fichier à écrire.
        contenu (str): Contenu à écrire dans le fichier.
    """
    with open(nom_fichier, 'w', encoding='utf-8') as fichier:
        fichier.write(contenu)

def nettoyer_chaine(chaine):
    """
    Nettoie une chaîne de caractères en supprimant les espaces de début et de fin.

    Args:
        chaine (str): Chaîne à nettoyer.

    Returns:
        str: Chaîne nettoyée.
    """
    return chaine.strip()

if __name__ == "__main__":
    print("Module utils_improved importé avec succès")
    print(lire_fichier("exemple.txt"))  # Remplacez "exemple.txt" par un fichier existant
    ecrire_fichier("exemple_ecrit.txt", "Contenu à écrire")
    print(nettoyer_chaine("   Chaîne à nettoyer   "))