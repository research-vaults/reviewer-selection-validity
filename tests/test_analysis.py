import importlib.util
import itertools
from pathlib import Path
import unittest
import numpy as np
from scipy.stats import rankdata
from scipy.optimize import linprog

spec = importlib.util.spec_from_file_location('replay', Path(__file__).resolve().parents[1]/'scripts/replay_results.py')
replay = importlib.util.module_from_spec(spec)
spec.loader.exec_module(replay)

class AnalysisTests(unittest.TestCase):
    def test_budget_conservation(self):
        scores = np.array([4., 3., 3., 3., 1.])
        for k in range(1, 6):
            w = replay.weights(scores, k)
            self.assertAlmostEqual(w.sum(), k)
            self.assertTrue(np.all((w >= 0) & (w <= 1)))

    def test_fractional_tie_enumeration(self):
        scores = np.array([4., 3., 3., 3., 1.])
        y = np.array([1., 1., 0., 0., 1.])
        exact = np.mean([y[[0, *choice]].mean() for choice in itertools.combinations([1, 2, 3], 2)])
        self.assertAlmostEqual(replay.weights(scores, 3) @ y / 3, exact)

    def test_permutation_invariance(self):
        s = np.array([4., 3., 3., 2., 1.])
        y = np.array([1., 0., 1., 1., 0.])
        p = np.array([3, 0, 4, 1, 2])
        self.assertAlmostEqual(replay.weights(s, 2) @ y, replay.weights(s[p], 2) @ y[p])

    def test_all_tied(self):
        np.testing.assert_allclose(replay.weights(np.ones(6), 2), np.full(6, 1/3))

    def test_rank_residualization_qr(self):
        rng = np.random.default_rng(4)
        z = rng.normal(size=(35, 2))
        x, y = rng.normal(size=(2, 35))
        design = np.column_stack([np.ones(35), z])
        q, _ = np.linalg.qr(design)
        ranks = np.column_stack([rankdata(x), rankdata(y)])
        residuals = ranks - q @ (q.T @ ranks)
        expected = np.corrcoef(residuals.T)[0, 1]
        self.assertAlmostEqual(replay.partial(x, y, z), expected, places=12)

    def test_missing_outcome_bounds(self):
        a, b = np.array([4., 3., 2., 1.]), np.array([1., 4., 3., 2.])
        d = (replay.weights(a, 2)-replay.weights(b, 2))/2
        observed = np.array([True, False, True, False])
        fixed = d[observed] @ np.array([1., 0.])
        missing = d[~observed]
        bound = [fixed+np.minimum(missing, 0).sum(), fixed+np.maximum(missing, 0).sum()]
        exhaustive = [fixed+missing @ np.array(v) for v in itertools.product([0., 1.], repeat=2)]
        np.testing.assert_allclose(bound, [min(exhaustive), max(exhaustive)])
        lo = linprog(missing, bounds=(0, 1), method='highs')
        hi = linprog(-missing, bounds=(0, 1), method='highs')
        self.assertTrue(lo.success and hi.success)
        np.testing.assert_allclose(bound, [fixed+lo.fun, fixed-hi.fun])

if __name__ == '__main__':
    unittest.main()
