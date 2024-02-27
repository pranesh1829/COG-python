def generate_fibonacci_sequence(terms):
    fibonacci_sequence = []

    if terms == 0:
        return fibonacci_sequence

    a, b = 0, 1
    fibonacci_sequence.append(a)

    for _ in range(terms - 1):
        a, b = b, a + b
        fibonacci_sequence.append(a)

    return fibonacci_sequence

def main():
    try:
        terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
        if terms < 0:
            raise ValueError("Number of terms should be a non-negative integer.")
        
        result = generate_fibonacci_sequence(terms)
        print(f"Fibonacci sequence up to {terms} terms: {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
