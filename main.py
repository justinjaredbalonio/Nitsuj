# main.py
import number_operations

# Define the main function
def main():
    num = int(input("Enter a number: "))
    print(f"The number {num} is {number_operations.is_even_or_odd(num)}.")
    if number_operations.is_prime(num):
        print(f"The number {num} is prime.")
    else:
        print(f"The number {num} is not prime.")
    if number_operations.is_palindrome(num):
        print(f"The number {num} is a palindrome.")
    else:
        print(f"The number {num} is not a palindrome.")

# Call the main function to start the program
if __name__ == "__main__":
    main()
