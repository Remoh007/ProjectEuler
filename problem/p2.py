import timeit
import __init__
from modules.fibonacci import *


def solution():
    """
    Solution for the Project Euler problem #2.

    Source: https://projecteuler.net/problem=2

    Modules used:
    fibonnaci
    """
    # Create a list of fibonacci numbers up to 4.000.000
    all_numbers = fibonacci.create_to_threshold(4000000)
    even_numbers = [x for x in all_numbers if x % 2 == 0]
    print("Solution: {}".format(sum(even_numbers)))


if __name__ == '__main__':
    runtime = timeit.timeit(solution, number=1)
    print("Runtime: {} milliseconds".format(runtime*1000))
