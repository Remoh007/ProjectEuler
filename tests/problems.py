import unittest
import timeit
import __init__
from problem.p1 import solution as solution_1
from problem.p2 import solution as solution_2


class TestProblemSolutions(unittest.TestCase):
    """Tests for the correct solution for each problem"""

    def test_problem_1(self):
        """Testing the solution for problem #1"""
        self.assertEqual(solution_1(), 233168)

    def test_problem_2(self):
        """Testing the solution for problem #2"""
        self.assertEqual(solution_2(), 4613732)


class TestProblemRuntimes(unittest.TestCase):
    """Tests for the runtime of each solution"""

    def test_runtime_problem_1(self):
        """Testing the runtime of problem #1"""
        runtime = timeit.timeit(solution_1, number=1)
        self.assertLessEqual(runtime, 0.01)

    def test_runtime_problem_2(self):
        """Testing the runtime of problem #2"""
        runtime = timeit.timeit(solution_2, number=1)
        self.assertLessEqual(runtime, 0.01)


if __name__ == '__main__':
    unittest.main()
