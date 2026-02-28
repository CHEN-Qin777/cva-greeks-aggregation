# -*- coding: utf-8 -*-
"""Agrégation des Grecques CVA pour un portefeuille d'options."""
import numpy as np
from .cva_greeks import cva_delta, cva_vega
from .cva import calculer_cva_simple

class PortefeuilleCVA:
    def __init__(self):
        self.positions = []  # chaque élément : (quantité, S0, K, T, r, sigma, spread_cds)

    def ajouter_position(self, quantite, S0, K, T, r, sigma, spread_cds):
        self.positions.append((quantite, S0, K, T, r, sigma, spread_cds))

    def calculer_cva_totale(self, n_steps=20, n_paths=5000):
        cva_total = 0
        for q, S0, K, T, r, sigma, spread_cds in self.positions:
            cva = calculer_cva_simple(S0, K, T, r, sigma, spread_cds, n_steps, n_paths)
            cva_total += q * cva
        return cva_total

    def calculer_grecques_agregees(self, n_steps=20, n_paths=5000, eps=0.01):
        delta_total = 0
        vega_total = 0
        for q, S0, K, T, r, sigma, spread_cds in self.positions:
            delta = cva_delta(S0, K, T, r, sigma, spread_cds, eps, n_steps, n_paths)
            vega = cva_vega(S0, K, T, r, sigma, spread_cds, eps, n_steps, n_paths)
            delta_total += q * delta
            vega_total += q * vega
        return {'delta_cva': delta_total, 'vega_cva': vega_total}
