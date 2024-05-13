# 22) Permutation and Combination Program

import math

def permutation(n, r):
    """
    Calculate the permutation of n objects taken r at a time.
    
    Parameters:
        n (int): Total number of objects.
        r (int): Number of objects to be taken.
    
    Returns:
        int: Permutation of n objects taken r at a time.
    """
    return math.factorial(n) // math.factorial(n - r)

def combination(n, r):
    """
    Calculate the combination of n objects taken r at a time.
    
    Parameters:
        n (int): Total number of objects.
        r (int): Number of objects to be taken.
    
    Returns:
        int: Combination of n objects taken r at a time.
    """
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

# Test cases
n = 5
r = 3
print("Permutation:", permutation(n, r))  # Output: 60
print("Combination:", combination(n, r))  # Output: 10
