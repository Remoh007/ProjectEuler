import unittest
import __init__
from modules.prime import *


class TestPrimeModule(unittest.TestCase):
    """Tests for prime module"""

    def test_factorize(self):
        """Testing the correct factorization of a number into all its prime factors"""
        self.assertEqual(prime.factors(2), [2])
        self.assertEqual(prime.factors(3), [3])
        self.assertEqual(prime.factors(45), [3, 3, 5])
        self.assertEqual(prime.factors(20), [2, 2, 5])
        self.assertEqual(prime.factors(13195), [5, 7, 13, 29])
        self.assertEqual(prime.factors(600851475143), [71, 839, 1471, 6857])

    def test_factorize_distinctive(self):
        """Testing that only distinctive prime factors are returned"""
        self.assertEqual(prime.distinct_factors(2), [2])
        self.assertEqual(prime.distinct_factors(3), [3])
        self.assertEqual(prime.distinct_factors(45), [3, 5])
        self.assertEqual(prime.distinct_factors(20), [2, 5])
        self.assertEqual(prime.distinct_factors(13195), [5, 7, 13, 29])
        self.assertEqual(prime.distinct_factors(
            600851475143), [71, 839, 1471, 6857])


if __name__ == '__main__':
    unittest.main()
