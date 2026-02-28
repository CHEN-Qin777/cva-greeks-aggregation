# -*- coding: utf-8 -*-
"""Calcul des Grecques de la CVA par différences finies."""
import numpy as np
from .cva import calculer_cva_simple

def cva_delta(S0, K, T, r, sigma, spread_cds, eps=0.01, n_steps=20, n_paths=5000):
    """Delta de la CVA = dCVA/dS0."""
    cva0 = calculer_cva_simple(S0, K, T, r, sigma, spread_cds, n_steps, n_paths)
    cva_up = calculer_cva_simple(S0+eps, K, T, r, sigma, spread_cds, n_steps, n_paths)
    cva_down = calculer_cva_simple(S0-eps, K, T, r, sigma, spread_cds, n_steps, n_paths)
    return (cva_up - cva_down) / (2*eps)

def cva_vega(S0, K, T, r, sigma, spread_cds, eps=0.001, n_steps=20, n_paths=5000):
    """Vega de la CVA = dCVA/dsigma."""
    cva0 = calculer_cva_simple(S0, K, T, r, sigma, spread_cds, n_steps, n_paths)
    cva_up = calculer_cva_simple(S0, K, T, r, sigma+eps, spread_cds, n_steps, n_paths)
    return (cva_up - cva0) / eps
