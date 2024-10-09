import math

def is_prime(n):
    try:
        n = int(n)  # Ensures the value passed is an integer
    except ValueError:
        print("Please enter a valid number.\n")
        return False

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check for factors up to the square root of n, skipping even numbers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    while True:
        number = input("Enter a number to check if it's prime (or 'q' to quit): ")
        if number.lower() == 'q':
            print("Exiting...")
            break  # Exit the loop if the user enters 'q'

        if is_prime(number):
            print(f"{number} is a prime number\n")
        else:
            print(f"{number} is not a prime number\n")

