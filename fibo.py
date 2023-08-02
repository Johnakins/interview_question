def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence

if __name__ == "__main__":
    n = 50  # Number of Fibonacci numbers to generate
    fibonacci_sequence = generate_fibonacci(n)

    # Sum the first 50 Fibonacci numbers
    fibonacci_sum = sum(fibonacci_sequence)

    print("Fibonacci sequence:")
    print(fibonacci_sequence)

    print(f"\nSum of the first 50 Fibonacci numbers: {fibonacci_sum}")
