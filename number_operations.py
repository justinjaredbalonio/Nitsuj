# number_operations.py

# Define a function to check if a number is even or odd
def is_even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

# Define a function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Define a function to check if a number is a palindrome
def is_palindrome(num):
    return str(num) == str(num)[::-1]
