import random

def generate_random_binary():
    binary_digits = [str(random.randint(0, 1)) for _ in range(4)]
    binary_number = "".join(binary_digits)
    return binary_number

def binary_to_decimal(binary_number):
    decimal_number = int(binary_number, 2)
    return decimal_number

if __name__ == "__main__":
    # Generate a random 4-digit binary number
    random_binary = generate_random_binary()
    
    # Convert the binary number to decimal
    decimal_number = binary_to_decimal(random_binary)
    
    print(f"Random 4-digit binary number: {random_binary}")
    print(f"Decimal equivalent: {decimal_number}")
