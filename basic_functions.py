"""
1.	Define a function greet_user that takes a name (string) as a parameter and prints a greeting
"""
def greet_user(username):
    # Ask the user to type their name
    username = input("Enter your name: ")

    # Greet without name if there is no input
    if username == None:
        print("Hello! Welcome!")
    else:
        # Greet the user using their name
        print(f"Hello {username}! Welcome!")

# greet_user(username="")

"""
2.	Define a function add_two_numbers that returns the sum of two numbers a and b.
    Returns the sum of two numbers a and b.
"""
def add_two_numbers(a, b):  
    return a + b
    
while True:
    try:
        a = float(input("Enter the first number -> a:"))
        b = float(input("Enter the second number -> b:"))
    except ValueError:
        print("Invalid input, you need to enter two numbers")
        continue
    else:
        thesum = add_two_numbers(a, b)

        print("The sum of the two numbers is:", thesum)
        print("--------------------------------")
        break
   
# add_two_numbers(a,b)

def is_even(num):
    """
    Define a function is_even(num) that returns True if num is even or False otherwise.
    """
    try:
        num = int(num)
    except ValueError:
        raise ValueError("Invalid input, you need to enter a valid number")
    return num % 2 == 0

while True:
    num = input("Enter a number ")
    try:
        result = is_even(num)
    except ValueError:
        print("Invalid input, you need to enter a valid number")
        continue

    print(f"{num} is {'an even' if result else 'an odd'} number")
    print("--------------------------------")
    break

# is_even(num)
is_even(num)
add_two_numbers(a,b)
greet_user(username="")