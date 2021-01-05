from math import sqrt


class prime:
    """
    This is a class for operations concerning prime numbers.
    """

    def factors(number):
        """
        Creates a list with all prime factors for a given number.

        Notice: Factors can be counted multiple times. 20 => [2,2,5]

        Parameters:
            number (int): Number on which the factors are searched

        Returns:
            List: A list with all prime factors
        """
        rest = number
        primefactors = []
        # Get all multiplies of 2
        while rest % 2 == 0 and rest != 2:
            primefactors.append(2)
            rest = int(rest/2)
        # Go though all uneven numbers
        n = 3
        while n < sqrt(rest):
            if rest % n == 0:
                primefactors.append(n)
                rest = int(rest / n)
                n = 3
            else:
                n += 2
        primefactors.append(rest)
        return primefactors

    def distinct_factors(number):
        """
        Creates a list with all distinctive prime factors for a given number.

        Parameters:
            number (int): Number on which the factors are searched

        Returns:
            List: A list with all distinctive prime factors
        """
        factors = list(set(prime.factors(number)))
        factors.sort()
        return factors
