#!/usr/bin/env python3
# coding: utf-8

"""
Module principal pour le projet test-ir-shell.
Ce module fournit les fonctionnalités de base pour l'interaction avec l'interface de commande.
"""

def afficher_menu():
    """
    Affiche le menu principal de l'application.

    Cette fonction affiche les options disponibles pour l'utilisateur.
    """
    print("Menu principal :")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Quitter")

def traiter_option(option):
    """
    Traite l'option sélectionnée par l'utilisateur.

    Args:
        option (int): L'option sélectionnée.

    Returns:
        str: Le résultat de l'option sélectionnée.
    """
    if option == 1:
        return "Option 1 sélectionnée"
    elif option == 2:
        return "Option 2 sélectionnée"
    else:
        return "Option invalide"

def demander_option():
    """
    Demande à l'utilisateur de sélectionner une option.

    Returns:
        int: L'option sélectionnée.
    """
    while True:
        try:
            option = int(input("Sélectionnez une option : "))
            if option < 1 or option > 3:
                print("Option invalide. Veuillez sélectionner une option entre 1 et 3.")
            else:
                return option
        except ValueError:
            print("Erreur de saisie. Veuillez sélectionner une option valide.")

if __name__ == "__main__":
    afficher_menu()
    option = demander_option()
    if option == 3:
        print("Au revoir !")
    else:
        print(traiter_option(option))