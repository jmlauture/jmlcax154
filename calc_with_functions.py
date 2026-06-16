# calc_with_functions.py
# Refactored simple calculator script using functions and exception handling


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b. Raise an error if b is zero."""
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b


def calculate(a, b, op):
    """Call the correct operation function based on the operation symbol."""
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        try:
            return divide(a, b)
        except ZeroDivisionError as error:
            return f"Error: {error}"
    else:
        return "Error: Invalid operation selected."


while True:
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        continue

    op = input("Choose an operation (+, -, *, /): ")

    result = calculate(number1, number2, op)

    print(f"The result between your first number {number1} "
          f"and your second number {number2} is {result}")

    answer = input("Do you want to perform another calculation? (yes/no): ")
    if answer.lower() != "yes":
        print("Thank you for using the simple calculator. Goodbye!")
        break
