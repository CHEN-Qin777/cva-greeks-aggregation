# -*- coding: utf-8 -*-
"""Génération de courbes de taux et de défaut."""
import numpy as np

def courbe_taux_constante(r, T, n_points):
    """Génère une courbe de taux constante."""
    temps = np.linspace(0, T, n_points)
    facteurs = np.exp(-r * temps)
    return temps, facteurs

def courbe_defaut_constante(lambda_def, T, n_points):
    """Génère une courbe de survie et probas de défaut."""
    temps = np.linspace(0, T, n_points)
    survie = np.exp(-lambda_def * temps)
    proba_def = 1 - survie
    proba_marg = np.diff(proba_def)
    return temps, survie, proba_marg
