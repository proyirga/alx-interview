#!/usr/bin/python3
"""
0-minoperations.py
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in
    exactly n 'H' characters in the file.

    :param n: The target number of 'H' characters.
    :type n: int
    :Return: The minimum number of operations needed.
    :Rtype: int
    """
    # Base case: If n is less than or equal to 1, it's impossible to achieve.
    if n <= 1:
        return 0

    # Initialize the minimum number of operations
    min_ops = 0

    # Find prime factorization
    factor = 2
    while n > 1:
        while n % factor == 0:
            min_ops += factor
            n //= factor
        factor += 1

    return min_ops
