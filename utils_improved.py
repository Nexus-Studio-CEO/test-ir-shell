#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module utils_improved pour le projet test-ir-shell.
Ce module fournit des fonctions utiles pour le projet.
"""

def ajout_element liste, element):
    """
    Ajoute un élément à la fin d'une liste.

    Args:
        liste (list): La liste à laquelle ajouter l'élément.
        element: L'élément à ajouter.

    Returns:
        list: La liste mise à jour.
    """
    liste.append(element)
    return liste

def supprimer_element liste, element:
    """
    Supprime la première occurrence d'un élément dans une liste.

    Args:
        liste (list): La liste à partir de laquelle supprimer l'élément.
        element: L'élément à supprimer.

    Returns:
        list: La liste mise à jour.
    """
    if element in liste:
        liste.remove(element)
    return liste

def trouver_index liste, element:
    """
    Trouve l'index de la première occurrence d'un élément dans une liste.

    Args:
        liste (list): La liste à partir de laquelle trouver l'index.
        element: L'élément à trouver.

    Returns:
        int: L'index de l'élément si trouvé, -1 sinon.
    """
    try:
        return liste.index(element)
    except ValueError:
        return -1

if __name__ == "__main__":
    ma_liste = [1, 2, 3]
    print(ajout_element(ma_liste, 4))  # [1, 2, 3, 4]
    print(supprimer_element(ma_liste, 2))  # [1, 3, 4]
    print(trouver_index(ma_liste, 3))  # 1
    print(trouver_index(ma_liste, 2))  # -1