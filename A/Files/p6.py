def is_prime(num):
    """
    Function to check if a number is prime.
    """
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        # Check divisibility up to the square root of the number
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

def print_first_n_primes(n):
    """
    Function to print the first n prime numbers.
    """
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num, end=" ")
            count += 1
        num += 1

# Print the first 100 prime numbers
print_first_n_primes(100)
