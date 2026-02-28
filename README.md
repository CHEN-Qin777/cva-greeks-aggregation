
# Calcul de CVA et agrégation des Grecques associées



## 📌 À propos

**CVA et agrégation des Grecques**  
Calcul de la CVA (Credit Valuation Adjustment) pour des options européennes par simulation Monte Carlo, avec calcul des expositions futures et agrégation des Grecques de CVA (Delta, Vega). Implémentation en Python.

## 📋 Description détaillée

Ce projet implémente le calcul de la **CVA** (Credit Valuation Adjustment) pour un call européen, en utilisant une simulation Monte Carlo des prix du sous-jacent (GBM) et un modèle de défaut à intensité constante. Il calcule également les **Grecques de la CVA** (Delta et Vega) par différences finies, et permet d'agréger ces risques pour un portefeuille de plusieurs options.

La CVA représente l'ajustement de la valeur d'un dérivé pour tenir compte du risque de défaut de la contrepartie. Son calcul nécessite :

- La simulation des expositions futures (valeur du dérivé à chaque date).
- La probabilité de défaut de la contrepartie (déduite des spreads CDS).
- L'actualisation des pertes attendues.

## ✨ Fonctionnalités

- ✅ Simulation de trajectoires GBM pour le sous-jacent.
- ✅ Calcul de l'exposition future d'un call européen (valeur intrinsèque).
- ✅ Calcul de la CVA avec probabilité de défaut constante.
- ✅ Calcul du Delta et du Vega de la CVA par différences finies.
- ✅ Agrégation des Grecques CVA pour un portefeuille multi-options.
- ✅ Visualisation de l'exposition attendue et de la distribution des pertes.
- ✅ Code modulaire, testé et documenté.

## 🔧 Installation

```bash
pip install -r requirements.txt
```

## 🚀 Utilisation

### Version locale
Exécutez les scripts dans l'ordre ou utilisez les modules dans votre propre code.

### Version Colab
Ouvrez le notebook [`cva_analyse_complete.ipynb`](notebooks/cva_analyse_complete.ipynb) dans Google Colab et exécutez toutes les cellules.

## 📊 Résultats obtenus

Les résultats suivants ont été obtenus avec les paramètres :
- `S0 = 100`, `K = 100`, `T = 1 an`, `r = 2%`, `sigma = 20%`, `spread_cds = 100 points de base`, `n_steps = 20`, `n_paths = 5000`, graine aléatoire fixée à 42.

| Mesure | Valeur |
|--------|--------|
| **CVA estimée** | 0,059021 |
| **Delta de la CVA** | 0,005316 |
| **Vega de la CVA**  | 0,411954 |

**Pour un portefeuille de 2 calls identiques :**

| Mesure | Valeur |
|--------|--------|
| **CVA totale du portefeuille** | 0,118043 |
| **Delta total CVA** | 0,010631 |
| **Vega total CVA**  | 0,823908 |

### Exposition attendue (Expected Exposure)

La figure ci‑dessous montre l'évolution de l'exposition attendue (moyenne sur toutes les simulations) en fonction du temps.

![Exposition attendue](results/ee.png)

(L'exposition augmente avec le temps car l'option a plus de chances de finir dans la monnaie, puis diminue légèrement en fin de vie à cause de l'actualisation.)

## 📁 Structure du projet

```
cva-greeks-aggregation/
├── README.md
├── requirements.txt
├── data/
│   ├── recuperer_cds.py          # (esquisse) récupération de spreads CDS
│   └── generer_courbes.py        # génération de courbes de taux/defaut
├── src/
│   ├── models/
│   │   ├── gbm.py                 # Simulation GBM
│   │   └── hull_white.py          # (esquisse) modèle de taux
│   ├── exposition.py              # Calcul de l'exposition
│   ├── cva.py                     # Calcul de la CVA
│   ├── cva_greeks.py              # Grecques de la CVA
│   └── portefeuille_cva.py        # Agrégation pour portefeuille
├── notebooks/
│   └── cva_analyse_complete.ipynb # Notebook Colab complet
├── results/
│   └── (figures générées)
└── tests/
    └── test_cva.py                 # Tests unitaires
```

## 📄 Licence

Projet éducatif – libre utilisation.

## 👤 Auteur

Étudiant en Master 2 Mathématiques Financières.

---

## ⚠️ Note sur la reproductibilité

Les résultats ci‑dessus sont obtenus avec une graine aléatoire fixée (`np.random.seed(42)`). Si vous exécutez le code sans fixer la graine, les valeurs peuvent légèrement varier.

---

## requirements.txt

```
numpy
scipy
matplotlib
pandas
```

---

