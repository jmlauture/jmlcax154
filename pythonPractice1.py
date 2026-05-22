# Using print() function to display output
print ("Hello, World!")
print()
print('Hello, World!')
print()


# Formatting output
print("""We're just ordinary people We don't know which way to go, yeah, hey 'Cause were ordinary people Maybe we should take it slow, hey, hey We're just ordinary people We don't know which way to go 'Cause we're ordinary people Maybe we should take it slow""")
print()

# Formatting output with escape character "\" for new line
print("We're just ordinary people \n We don't know which way to go, \n yeah, hey 'Cause were ordinary people \n Maybe we should take it slow, hey, hey \n We're just ordinary people We don't know which way to go \n 'Cause we're ordinary people Maybe we should take it slow")
print()

# Combining two lines of code into one line
print("My name is Bond", end=" ")
print("James Bond.")

print()

# Using separators value in print() function
print("apple", "banana", "cherry", sep=", ")
print("apple", "banana", "cherry", sep="-")
print("apple", "banana", "cherry", sep="*")

#Printing literal values
print(27)
print(3.14)

#Printing boolean values
print(True)
print(False)
print(True > False)
print(False < True)
print(True < False)

#Working with operators
print(10 + 5)  # Addition
print(10 - 5)  # Subtraction
print(10 * 5)  # Multiplication
print(10 / 5)  # Division - results in float
print(10 // 5) # Floor Division - results in integer 
print(10 % 5)  # Modulus
print(10 % 3)  # Modulus -results in remainder
print(10 ** 5) # Exponentiation - results in 10 raised to the power of 5

# Order of operations -pedmas- parentheses, exponents, multiplication/division, addition/subtraction
print(2 + 3 * 4)  # Multiplication is performed first
print((2 + 3) * 4)  # Parentheses change the order of operations
print(10 - 2 ** 3)  # Exponentiation is performed first
print((10 - 2) ** 3)  # Parentheses change the order of operations

# Using variables to store values
x = 10
y = 5
print(x + y)  # Addition using variables
print(x - y)  # Subtraction using variables
print(x * y)  # Multiplication using variables
print(x / y)  # Division using variables
print(x // y) # Floor Division using variables
print(x % y)  # Modulus using variables
print(x ** y) # Exponentiation using variables

name="John"
age = 30
height = 6.1
print("My name is", name, "and I am", age, "years old. I am", height, "feet tall.")
print(f"My name is {name} and I am {age} years old. I am {height} feet tall.")
print("My name is {} and I am {} years old. I am {} feet tall.".format(name, age, height))
print("My name is " + name + " and I am " + str(age) + " years old. I am " + str(height) + " feet tall.")

# Inputting variables from user
name = input("What is your name? ")
age = input("What is your age? ")
print("Hello, " + name + "! You are " + age + " years old.")
