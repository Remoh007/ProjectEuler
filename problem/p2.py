import timeit
try:
    from modules.fibonacci import *
except ModuleNotFoundError:
    from problem.modules.fibonacci import *


def solution():
    all_numbers = fibonacci.create_to_threshold(4000000)
    even_numbers = [x for x in all_numbers if x % 2 == 0]
    print("Solution: {}".format(sum(even_numbers)))


if __name__ == '__main__':
    runtime = timeit.timeit(solution, number=1)
    print("Runtime: {} milliseconds".format(runtime*1000))
