import unittest
import numpy as np
from src.cva import calculer_cva_simple

class TestCVA(unittest.TestCase):
    def test_cva_call(self):
        cva = calculer_cva_simple(100, 100, 1, 0.02, 0.2, 0.01, n_steps=10, n_paths=1000)
        self.assertTrue(np.isfinite(cva))
        self.assertGreater(cva, 0)

if __name__ == '__main__':
    unittest.main()
