#!/usr/bin/python3
"""
Minimum operations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    Args:
        n (int): The desired number of H characters in the file. 
    Returns:
        int: The minimum number of operations required
        to reach n H characters.
    Notes:
        If n is impossible to achieve, the function returns 0.
    """
    if n <= 1:
        return 0
    operations = 0
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1
    return operations
