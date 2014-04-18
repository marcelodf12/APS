from django.test import TestCase

import doctest

def factorial(n):
    """
    >>> factorial(3)
    6
    >>> factorial(4)
    24
    >>> factorial(5)
    120
    """
    return 1 if n < 1 else n * factorial(n-1)


if __name__ == "__main__":
    doctest.testmod()