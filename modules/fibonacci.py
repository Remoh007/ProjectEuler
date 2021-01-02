from math import sqrt, pow


class fibonacci:
    """
    This is a class for operations concerning fibonacci numbers.
    """

    def create_to_threshold(threshold):
        """
        Creates a list with all fibonacci numbers up to given threashold.

        Parameters:
            threshold (int): The threshold of the largest fibonacci number

        Returns:
            List: A list with fibonacci numbers
        """

        fibonaccis = [0, 1]
        while fibonaccis[-1] < threshold:
            fibonaccis.append(fibonaccis[-1]+fibonaccis[-2])
        del fibonaccis[-1]

        return fibonaccis

    def create_to_nth(n):
        """
        Creates a list with all fibonacci numbers up to the nth fibonacci number.

        Parameters:
            n (int): Index of the largest fibonacci number

        Returns:
            List: A list with fibonacci numbers
        """

        if n == 0:
            return [0]
        if n == 1:
            return [1]

        fibonaccis = [0, 1]
        while len(fibonaccis) < n:
            fibonaccis.append(fibonaccis[-1]+fibonaccis[-2])
        return fibonaccis

    def get(n):
        """
        The function to calculate a fibonacci number.

        It is using the Moivre-Binet formula.

        Parameters:
            n (int): Index of the fibonacci number

        Returns:
            Int: A fibonacci number
        """

        return int(1/sqrt(5) * (pow((1+sqrt(5))/2, n) - pow((1-sqrt(5))/2, n)))
