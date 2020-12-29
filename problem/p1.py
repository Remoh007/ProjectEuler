import timeit


def solution():
    # Find multiplies of 3 or 5
    multiplies = []
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            multiplies.append(i)
    # Calculating the sum of a list
    result = sum(multiplies)
    print("The sum of all multiplies of 3 or 5 below 1000 is {}".format(result))
    # => Runtime: 0.2972510000000001 milliseconds


def solution_1():
    # Using list comprehension to increase the speed?
    result = sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])
    print("The sum of all multiplies of 3 or 5 below 1000 is {}".format(result))


if __name__ == '__main__':
    runtime = timeit.timeit(solution, number=1)
    print("Runtime: {} milliseconds".format(runtime*1000))
