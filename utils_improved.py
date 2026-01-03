#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module d'utilitaires pour le projet test-ir-shell.
Ce module fournit diverses fonctions pour faciliter le développement et la maintenance du projet.
"""

def extraire_entite(nom_fichier):
    """
    Extrait l'entité d'un fichier en fonction de son nom.

    Args:
        nom_fichier (str): Le nom du fichier.

    Returns:
        str: L'entité extraite du nom du fichier.
    """
    return nom_fichier.split('.')[0]

def convertir_temperature(celsius):
    """
    Convertit une température de Celsius en Fahrenheit.

    Args:
        celsius (float): La température en Celsius.

    Returns:
        float: La température en Fahrenheit.
    """
    return (celsius * 9/5) + 32

def formater_chaine(chaine, longueur):
    """
    Formate une chaîne de caractères pour qu'elle soit de la longueur spécifiée.

    Args:
        chaine (str): La chaîne à formater.
        longueur (int): La longueur souhaitée pour la chaîne.

    Returns:
        str: La chaîne formattée.
    """
    if len(chaine) > longueur:
        return chaine[:longueur]
    else:
        return chaine.ljust(longueur)

if __name__ == "__main__":
    print(extraire_entite("exemple.txt"))
    print(convertir_temperature(30))
    print(formater_chaine("Bonjour, monde!", 10))