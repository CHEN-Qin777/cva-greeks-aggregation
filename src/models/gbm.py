# -*- coding: utf-8 -*-
"""Simulation de GBM pour le sous-jacent."""
import numpy as np

def simuler_gbm(S0, mu, sigma, T, n_steps, n_paths):
    """
    Simule des trajectoires GBM.
    Retourne un array (n_paths, n_steps+1)
    """
    dt = T / n_steps
    trajectoires = np.zeros((n_paths, n_steps+1))
    trajectoires[:,0] = S0
    for t in range(1, n_steps+1):
        z = np.random.normal(size=n_paths)
        trajectoires[:,t] = trajectoires[:,t-1] * np.exp((mu - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*z)
    return trajectoires
