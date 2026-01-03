#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module d'utilitaires pour le projet test-ir-shell.
Ce module fournit des fonctions pour faciliter les opérations courantes.
"""

def additionner(a, b):
    """
    Additionne deux nombres.

    Args:
        a (int): Le premier nombre.
        b (int): Le deuxième nombre.

    Returns:
        int: La somme des deux nombres.
    """
    return a + b

def soustraire(a, b):
    """
    Soustrait deux nombres.

    Args:
        a (int): Le premier nombre.
        b (int): Le deuxième nombre.

    Returns:
        int: La différence entre les deux nombres.
    """
    return a - b

def multiplier(a, b):
    """
    Multiplie deux nombres.

    Args:
        a (int): Le premier nombre.
        b (int): Le deuxième nombre.

    Returns:
        int: Le produit des deux nombres.
    """
    return a * b

if __name__ == "__main__":
    print(additionner(5, 3))  # Exemple d'utilisation de la fonction additionner
    print(soustraire(10, 4))   # Exemple d'utilisation de la fonction soustraire
    print(multiplier(7, 2))    # Exemple d'utilisation de la fonction multiplier