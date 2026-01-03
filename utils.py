#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module d'utilitaires pour le projet test-ir-shell.
"""

def convertir_en_majuscule(texte):
    """
    Convertit un texte en majuscule.

    Args:
        texte (str): Le texte à convertir.

    Returns:
        str: Le texte en majuscule.
    """
    return texte.upper()

def calculer_la_somme(nombres):
    """
    Calcule la somme d'une liste de nombres.

    Args:
        nombres (list): La liste de nombres.

    Returns:
        int: La somme des nombres.
    """
    return sum(nombres)

def est_un_nombre_premier(n):
    """
    Vérifie si un nombre est premier.

    Args:
        n (int): Le nombre à vérifier.

    Returns:
        bool: True si le nombre est premier, False sinon.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print(convertir_en_majuscule("bonjour"))
    nombres = [1, 2, 3, 4, 5]
    print(calculer_la_somme(nombres))
    print(est_un_nombre_premier(7))