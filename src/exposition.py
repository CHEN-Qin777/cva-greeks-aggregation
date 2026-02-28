# -*- coding: utf-8 -*-
"""Calcul de l'exposition future d'un dérivé."""
import numpy as np
from .models.gbm import simuler_gbm

def exposition_call_europeen(S0, K, T, r, sigma, n_steps, n_paths):
    """
    Simule les prix de l'actif et calcule l'exposition (valeur du call) à chaque date.
    Retourne une matrice (n_paths, n_steps+1) de l'exposition.
    """
    dt = T / n_steps
    trajectoires = simuler_gbm(S0, r, sigma, T, n_steps, n_paths)  # risque-neutre
    # Pour un call européen, on utilise la valeur intrinsèque comme proxy
    exposition = np.maximum(trajectoires - K, 0)
    return exposition
