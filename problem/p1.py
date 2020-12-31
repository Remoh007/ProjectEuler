import timeit


def solution():
    """
    Solution for the Project Euler problem #1.

    Source: https://projecteuler.net/problem=1
    """
    # Find multiplies of 3 or 5
    multiplies = []
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            multiplies.append(i)
    # Calculating the sum of a list
    result = sum(multiplies)
    print("The sum of all multiplies of 3 or 5 below 1000 is {}".format(result))


def solution_1():
    """
    Alternative Solution for the Project Euler problem #1.

    Source: https://projecteuler.net/problem=1
    Same logic as before but this uses python's list comprehension.
    """
    result = sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])
    print("The sum of all multiplies of 3 or 5 below 1000 is {}".format(result))


if __name__ == '__main__':
    runtime = timeit.timeit(solution, number=1)
    print("Runtime: {} milliseconds".format(runtime*1000))
