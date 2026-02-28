# -*- coding: utf-8 -*-
"""Calcul de la CVA."""
import numpy as np

def calculer_cva(exposition, probabilite_defaut, taux_recouvrement=0.4, facteur_actualisation=None):
    """
    Calcule la CVA.

    Paramètres
    ----------
    exposition : np.array (n_paths, n_temps)
        Exposition à chaque date (colonnes : temps 0, dt, 2dt, ..., T)
    probabilite_defaut : np.array (n_temps-1)
        Probabilités de défaut marginales entre chaque pas (taille n_temps-1)
    taux_recouvrement : float
        Taux de recouvrement en cas de défaut
    facteur_actualisation : np.array (n_temps)
        Facteurs d'actualisation aux mêmes dates que l'exposition (taille n_temps)

    Retour
    ------
    float : CVA
    """
    n_paths, n_temps = exposition.shape
    if facteur_actualisation is None:
        facteur_actualisation = np.ones(n_temps)

    EE = exposition.mean(axis=0)  # Expected Exposure, taille n_temps
    LGD = 1 - taux_recouvrement

    cva = LGD * np.sum(EE[1:] * probabilite_defaut * facteur_actualisation[1:])
    return cva

def calculer_cva_simple(S0, K, T, r, sigma, spread_cds, n_steps=50, n_paths=10000):
    """
    Calcule CVA pour un call européen avec spread CDS constant.
    """
    from .exposition import exposition_call_europeen

    expo = exposition_call_europeen(S0, K, T, r, sigma, n_steps, n_paths)

    lambda_def = spread_cds / (1 - 0.4)  # approximation LGD = 60%
    dt = T / n_steps
    t = np.arange(0, T, dt)  # débuts des intervalles, taille n_steps
    proba_def_marg = np.exp(-lambda_def * t) * (1 - np.exp(-lambda_def * dt))

    df = np.exp(-r * np.linspace(0, T, n_steps+1))

    cva = calculer_cva(expo, proba_def_marg, 0.4, df)
    return cva
