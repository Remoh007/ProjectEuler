from importlib import import_module
import timeit


def main():
    """
    Main entry to run solutions for solved Project Euler problems.

    Source: https://projecteuler.net
    """
    print("ProjectEuler Solutions by Remoh007")
    try:
        problem = int(input("Enter problem # "))
        try:
            # Load problem and run the solution
            p = import_module("problem.p{}".format(problem))
            print("Running solution for problem #{}".format(problem))
            runtime = timeit.timeit(p.solution, number=1)
            print("Runtime: {} milliseconds".format(runtime*1000))
        except ModuleNotFoundError:
            # Show error message if there is no script for the problem
            print("There is no solution for problem {}".format(problem))
    except ValueError:  # The input was not an integer
        print("You need to enter a valid number.")


if __name__ == "__main__":
    main()
