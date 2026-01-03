#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module d'utilitaires pour le projet test-ir-shell.

Ce module fournit des fonctions pour différents usages.
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

def est_premier(n):
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
    print(additionner(2, 3))  # Exemple d'utilisation de la fonction additionner
    print(multiplier(4, 5))  # Exemple d'utilisation de la fonction multiplier
    print(est_premier(7))  # Exemple d'utilisation de la fonction est_premier