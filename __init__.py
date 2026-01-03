#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module principal du projet test-ir-shell.

Ce module fournit les fonctionnalités de base pour le projet test-ir-shell.
Il contient des fonctions pour gérer les données et effectuer des opérations.
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
        int: La différence des deux nombres.
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
    print("Test du module test-ir-shell")
    print("Addition : 2 + 3 =", additionner(2, 3))
    print("Soustraction : 5 - 2 =", soustraire(5, 2))
    print("Multiplication : 4 * 6 =", multiplier(4, 6))