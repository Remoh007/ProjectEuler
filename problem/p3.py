import timeit
import __init__
from modules.prime import *


def solution():
    number = 600851475143
    all_factors = prime.factors(number)
    return max(all_factors)


if __name__ == '__main__':
    result = solution()
    print("Solution: {}".format(result))

    runtime = timeit.timeit(solution, number=1)
    print("Runtime: {} seconds".format(runtime))
