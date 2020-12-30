# Main file to run solutions for solved problems
from importlib import import_module
import timeit


def main():
    print("ProjectEuler Solutions by Remoh007")
    try:
        problem = int(input("Enter problem # "))
        try:
            p = import_module("problem.p{}".format(problem))
            print("Running solution for problem #{}".format(problem))
            runtime = timeit.timeit(p.solution, number=1)
            print("Runtime: {} milliseconds".format(runtime*1000))
        except ModuleNotFoundError as e:
            print(e)
            print("There is no solution for problem {}".format(problem))
    except ValueError:
        print("You need to enter a valid number.")


if __name__ == "__main__":
    main()
