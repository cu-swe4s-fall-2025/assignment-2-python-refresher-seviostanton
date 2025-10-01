import random
import unittest
import my_utils
import sys
import numpy as np


def random_list_uniform(n=25, lower=-1000, upper=1000, seed=0):
    """Generate a list of n random integers
    between lower and upper (inclusive).
    Args:
        n (int): Number of random integers to generate.
        lower (int): Lower bound for random integers.
        upper (int): Upper bound for random integers.
        seed (int): Seed for the random number generator.
    Returns:
        list: List of n random integers."""
    """
    Return a Python list of n random integers in [lower, upper], fast.
    """
    rng = np.random.default_rng(seed)
    int_list = rng.integers(lower, upper,
                            size=n, endpoint=True,
                            dtype=np.int64).tolist()
    return int_list


def random_list_normal(n=25, mu=0, sigma=1, seed=0):
    """Generate a list of n random integers from a normal distribution.
    Args:
        n (int): Number of random integers to generate.
        mu (float): Mean of the normal distribution.
        sigma (float): Standard deviation of the normal distribution.
        seed (int): Seed for the random number generator.
    Returns:
        list: List of n random integers."""
    rng = np.random.default_rng(seed)
    int_list = 1000*rng.normal(loc=mu, scale=sigma, size=n)
    return int_list.astype(np.int64).tolist()


class TestMean(unittest.TestCase):
    def test_mean_random_uniform(self):
        n = 10**7
        lower = -10**2
        upper = 10**2
        seed = 0
        tol = 0.1
        self.assertAlmostEqual(my_utils.mean_ints(
                                random_list_uniform(n=n,
                                                    lower=lower,
                                                    upper=upper,
                                                    seed=seed)
                                                    ), 0.0, delta=tol)

    def test_mean_random_normal(self):
        n = 10**7
        mu = 0
        sigma = 1
        seed = 0
        tol = 1
        self.assertAlmostEqual(my_utils.mean_ints(
                                random_list_normal(n=n,
                                                   mu=mu,
                                                   sigma=sigma,
                                                   seed=seed)
                                                   ), 0.0, delta=tol)

    def test_mean_empty_raises(self):
        with self.assertRaises(ValueError):
            my_utils.mean_ints([])

    def test_mean_large_list(self):
        large_list = random_list_uniform(n=10**6,
                                         lower=-10**3,
                                         upper=10**3,
                                         seed=42)
        expected_mean = sum(large_list) / len(large_list)
        self.assertAlmostEqual(my_utils.mean_ints(large_list),
                               expected_mean,
                               delta=1e-4)

    def test_mean_single_value(self):
        self.assertEqual(my_utils.mean_ints([42]), 42.0)


class TestMedian(unittest.TestCase):
    def test_median_random_uniform(self):
        n = 10**6
        lower = -10**2
        upper = 10**2
        seed = 0
        self.assertAlmostEqual(
                               my_utils.median_ints(
                                   random_list_uniform(n=n,
                                                       lower=lower,
                                                       upper=upper,
                                                       seed=seed)),
                               (upper+lower)/2.0, delta=1e-1
                               )

    def test_median_random_normal(self):
        n = 10**6
        mu = 0
        sigma = 1
        seed = 0
        tol = 1e-4
        self.assertAlmostEqual(my_utils.median_ints(
                                random_list_normal(n=n,
                                                   mu=mu,
                                                   sigma=sigma,
                                                   seed=seed)
                                                   ), 0.0, delta=tol)

    def test_median_empty_raises(self):
        with self.assertRaises(ValueError):
            my_utils.median_ints([])

    def test_median_odd_length(self):
        self.assertEqual(my_utils.median_ints([-3, -1, -2]), -2.0)

    def test_median_even_length(self):
        self.assertEqual(my_utils.median_ints([4, 1, 3, 2]), 2.5)

    def test_median_single_value(self):
        self.assertEqual(my_utils.median_ints([42]), 42.0)


class TestStd(unittest.TestCase):
    def test_std_random_normal(self):
        n = 10**6
        mu = 0
        sigma = 1
        seed = 0
        tol = 1
        self.assertAlmostEqual(my_utils.std_ints(
                                random_list_normal(n=n,
                                                   mu=mu,
                                                   sigma=sigma,
                                                   seed=seed)
                                                   ), 1.0*1000, delta=tol)

    def test_std_empty_raises(self):
        with self.assertRaises(ValueError):
            my_utils.std_ints([])

    def test_std_known_values(self):
        self.assertAlmostEqual(my_utils.std_ints([1, 2, 3, 4, 5]),
                               1.5811388300841898,
                               delta=1e-4)

    def test_std_single_value(self):
        self.assertRaises(ValueError, my_utils.std_ints, [42])


if __name__ == "__main__":
    unittest.main()
    sys.exit(0)
