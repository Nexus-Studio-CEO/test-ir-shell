#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module de configuration pour le projet test-ir-shell.
Ce module contient les fonctions de base pour la configuration et l'installation du projet.
"""

def configure_project():
    """
    Configure le projet en créant les répertoires et les fichiers nécessaires.
    
    Returns:
        None
    """
    import os
    project_dir = os.path.dirname(os.path.abspath(__file__))
    config_dir = os.path.join(project_dir, 'config')
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

def install_dependencies():
    """
    Installe les dépendances nécessaires pour le projet.
    
    Returns:
        None
    """
    import subprocess
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

def build_project():
    """
    Construit le projet en compilant les fichiers source et en créant les exécutables.
    
    Returns:
        None
    """
    import subprocess
    subprocess.run(['python', 'setup.py', 'build'])

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Configure et installe le projet test-ir-shell.')
    parser.add_argument('--configure', action='store_true', help='Configure le projet.')
    parser.add_argument('--install', action='store_true', help='Installe les dépendances.')
    parser.add_argument('--build', action='store_true', help='Construit le projet.')
    args = parser.parse_args()
    if args.configure:
        configure_project()
    if args.install:
        install_dependencies()
    if args.build:
        build_project()