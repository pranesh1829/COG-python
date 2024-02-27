def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

def calculate_percentage(x, y):
    return (x * y) / 100

def main():

    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /, %): ")
    num2 = float(input("Enter the second number: "))

    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    elif operator == '%':
        result = calculate_percentage(num1, num2)
    else:
        result = "Error: Invalid operator."

    print(f"The result of {num1} {operator} {num2} is: {result}")

if __name__ == "__main__":
    main()
