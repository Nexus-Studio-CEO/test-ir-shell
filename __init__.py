#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module principal du projet test-ir-shell.
Ce module fournit des fonctionnalités de base pour le projet.
"""

def afficher_message(message: str) -> None:
    """
    Affiche un message à l'écran.

    Args:
        message (str): Le message à afficher.
    """
    print(message)

def additionner(a: int, b: int) -> int:
    """
    Additionne deux nombres entiers.

    Args:
        a (int): Le premier nombre.
        b (int): Le deuxième nombre.

    Returns:
        int: La somme des deux nombres.
    """
    return a + b

def est_premier(n: int) -> bool:
    """
    Vérifie si un nombre est premier.

    Args:
        n (int): Le nombre à vérifier.

    Returns:
        bool: True si le nombre est premier, False sinon.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    afficher_message("Bonjour, monde!")
    result = additionner(2, 3)
    print(f"2 + 3 = {result}")
    print(f"Est-ce que 5 est premier ? {est_premier(5)}")