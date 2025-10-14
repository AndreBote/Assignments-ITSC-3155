"""
GOOD VERSION: Small CLI calculator demonstrating coding best practices.
Principles shown:
- KISS
- Single responsibility
- YAGNI
- Document Your Code
- DRY
"""


def add(a,b):
    """
    Return the sum of a and b.
    Parameters:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The result of a + b.
    """
    return a + b


def subtract(a, b):
    """
    Return the difference of a and b.
    Parameters:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The result of a - b.
    """
    return a - b


def multiply(a, b):
    """
    Return the product of a and b.
    Parameters:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The result of a * b.
    """
    return a * b


def divide(a, b):
    """
    Return quotient of a and b. Raises ValueError on division by zero.
    Parameters:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The result of a / b.
    """
    if a == 0:
        raise ValueError("Cannot divide with zero")
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def main():
    """
    Runs the simple calculator.
    - Prompts the user for two numbers and an operation.
    - Calls the appropriate math function based on the operator.
    - Prints the result or an error message.
    """
    while True:
        print("\nSimple Calculator (+, -, *, /)")
        q = input("Type 'quit' now to quit otherwise type anything else: ")
        if q == "quit":
            break

        try:
            a = float(input("Enter first number: "))
            op = input("Enter operation (+ - * /): ").strip()
            b = float(input("Enter second number: "))
        except ValueError:
            print("Error: inputs must be valid.")
            return

        try:
            if op == "+":
                result = add(a, b)
            elif op == "-":
                result = subtract(a, b)
            elif op == "*":
                result = multiply(a, b)
            elif op == "/":
                result = divide(a, b)
            else:
                print("Error: Unsupported operation.")
                continue
            print(f"Result: {result}")
        except ValueError as err:
            print(f"Error: {err}")

    print("Thank you for using, Good Calculator")


if __name__ == "__main__":
    main()
