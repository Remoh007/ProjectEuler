from math import sqrt, pow


class fibonacci:
    def create_to_threshold(threshold):
        """
        Creates a list with all fibonacci numbers up to given threashold.
        Arguments:
        threshold - integer of greatest fibonacci numbers

        Returns:
        fibonaccis - list including all fibonacci numbers
        """
        fibonaccis = [0, 1]
        while fibonaccis[-1] < threshold:
            fibonaccis.append(fibonaccis[-1]+fibonaccis[-2])
        del fibonaccis[-1]

        return fibonaccis

    def create_to_nth(n):
        """
        Creates a list with all fibonacci numbers up to the nth number.
        Arguments:
        n - integer of the nth fibonacci number

        Returns:
        fibonaccis - list including the first nth fibonacci numbers
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
        Returns the nth fibonacci number.
        """
        return int(1/sqrt(5) * (pow((1+sqrt(5))/2, n) - pow((1-sqrt(5))/2, n)))
