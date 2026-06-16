# Lab 351-2_2: User Interaction and Input 
# Author: Jean Lauture
# To see the outputs of this code, 
# run it in a Python environment (like VS Code, Jupyter Notebook, PyCharm, 
# or the command line) 
# python3 lab351-2_2_simple_calculator.py  
#

while True:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    op = input("Choose an operation (+, -, *, /): ")
    if op == "+":
        operation = "addition"
        result = number1 + number2
    elif op == "-":
        operation = "subtraction"
        result = number1 - number2
    elif op == "*":
        operation = "multiplication"
        result = number1 * number2
    elif op == "/":
        operation = "division"
        if number2 != 0:
            result = number1 / number2
        else:
            result = "Error: Division by zero is not allowed."
    else:
        operation = "unknown operation"
        result = "Error: Invalid operation selected."

    print(f"The result of the {operation} between your first number {number1} "
          f"and your second number {number2} is {result}")

    answer = input("Do you want to perform another calculation? (yes/no): ")
    if answer.lower() != "yes":
        print("Thank you for using the simple calculator. Goodbye!")
        break
